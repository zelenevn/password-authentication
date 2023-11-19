package com.ivancha.service;

import com.ivancha.interceptor.TransactionInterceptor;
import com.ivancha.mapper.PasswordCreateMapper;
import com.ivancha.mapper.PasswordReadMapper;
import com.ivancha.mapper.UserCreateMapper;
import com.ivancha.mapper.UserReadMapper;
import com.ivancha.repository.PasswordRepository;
import com.ivancha.repository.UserRepository;
import com.ivancha.util.HibernateUtil;
import jakarta.validation.Validation;
import jakarta.validation.Validator;
import lombok.experimental.UtilityClass;
import net.bytebuddy.ByteBuddy;
import net.bytebuddy.implementation.MethodDelegation;
import net.bytebuddy.matcher.ElementMatchers;
import org.hibernate.Session;
import org.hibernate.SessionFactory;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Proxy;


@UtilityClass
public class ServiceUtil {


    public static ServiceResources startServices() {
        SessionFactory sessionFactory = HibernateUtil.getSessionFactory();

        // прокси объект над сессией, чтобы не получать CurrentSession() через SessionFactory в методах Repository,
        // а получать возвращаемое CurrentSession() значение при обычном обращении к зависимости EntityManager внутри Repository.
        var proxySession = (Session) Proxy.newProxyInstance(SessionFactory.class.getClassLoader(), new Class[]{Session.class},
                (proxy, method, args1) -> method.invoke(sessionFactory.getCurrentSession(), args1));

        var validatorFactory = Validation.buildDefaultValidatorFactory();
        var validator = validatorFactory.getValidator();

        var passwordReadMapper = new PasswordReadMapper();
        var userReadMapper = new UserReadMapper(passwordReadMapper);
        var userCreateMapper = new UserCreateMapper();
        var userRepository = new UserRepository(proxySession);

        // Прокси объекты над сервисами, чтобы динамически открывать / закрывать транзакции в их методах, помеченных @Transactional.
        // И не прописывать эту логику в каждом методе вручную.
        var transactionInterceptor = new TransactionInterceptor(sessionFactory);

        try {
            UserService proxyUserService = loadTransactionHandlerProxy(UserService.class, transactionInterceptor)
                    .getDeclaredConstructor(UserRepository.class, UserCreateMapper.class, UserReadMapper.class, Validator.class)
                    .newInstance(userRepository, userCreateMapper, userReadMapper, validator);

            var passwordRepository = new PasswordRepository(proxySession);
            var passwordCreateMapper = new PasswordCreateMapper(userRepository);

            PasswordService proxyPasswordService = loadTransactionHandlerProxy(PasswordService.class, transactionInterceptor)
                    .getDeclaredConstructor(PasswordRepository.class, PasswordCreateMapper.class, Validator.class)
                    .newInstance(passwordRepository, passwordCreateMapper, validator);

            return new ServiceResources(proxyUserService, proxyPasswordService);

        } catch (InstantiationException |
                 IllegalAccessException |
                 InvocationTargetException |
                 NoSuchMethodException e) {
            throw new RuntimeException(e);
        }
    }

    public record ServiceResources(
            UserService userService,
            PasswordService passwordService
    ) {}


    private static <T> Class<? extends T> loadTransactionHandlerProxy(Class<T> subclass, TransactionInterceptor transactionInterceptor) {

        return new ByteBuddy()
                .subclass(subclass)
                .method(ElementMatchers.any())
                .intercept(MethodDelegation.to(transactionInterceptor))
                .make()
                .load(subclass.getClassLoader())
                .getLoaded();
    }
}

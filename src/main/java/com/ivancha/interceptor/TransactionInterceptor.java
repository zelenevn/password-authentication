package com.ivancha.interceptor;

import jakarta.transaction.Transactional;
import net.bytebuddy.implementation.bind.annotation.Origin;
import net.bytebuddy.implementation.bind.annotation.RuntimeType;
import net.bytebuddy.implementation.bind.annotation.SuperCall;
import lombok.RequiredArgsConstructor;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import java.lang.reflect.Method;
import java.util.concurrent.Callable;

@RequiredArgsConstructor
public class TransactionInterceptor
{

    private final SessionFactory sessionFactory;

    @RuntimeType
    public Object intercept(@SuperCall Callable<Object> call, @Origin Method method) throws Exception {
        Transaction transaction = null;
        // чтобы закрывать транзакцию на том же уровне, где её и открывали
        // например будет цепочка findById -> saveCompany -> saveLocales. Без этого закроем транзакцию на saveLocales
        boolean transactionStarted = false;
        if (method.isAnnotationPresent(Transactional.class))
        {
            transaction = sessionFactory.getCurrentSession().getTransaction();
            if (!transaction.isActive())
            {
                transaction.begin();
                transactionStarted = true;
            }
        }

        Object result;
        try
        {
            result = call.call();
            if (transactionStarted)
                transaction.commit();
        } catch (Exception e)
        {
            if (transactionStarted)
                transaction.rollback();

            throw e;
        }

        return result;
    }
}

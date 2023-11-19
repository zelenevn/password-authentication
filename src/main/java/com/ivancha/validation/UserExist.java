package com.ivancha.validation;

import com.ivancha.validation.impl.UserExistValidator;
import jakarta.validation.Constraint;
import jakarta.validation.Payload;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;


@Constraint(validatedBy = UserExistValidator.class)
@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
public @interface UserExist {

    String message() default "Пользователь с таким именем должен существовать";

    Class<?>[] groups() default { };

    Class<? extends Payload>[] payload() default { };
}

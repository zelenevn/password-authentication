package com.ivancha.validation;

import com.ivancha.validation.impl.PasswordStatValidator;
import jakarta.validation.Constraint;
import jakarta.validation.Payload;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;


@Constraint(validatedBy = PasswordStatValidator.class)
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
public @interface PasswordStatMatches {

    String message() default "Data :/ Предоставленные параметры ввода пароля не согласуются друг с другом";

    Class<?>[] groups() default { };

    Class<? extends Payload>[] payload() default { };
}

package com.ivancha.validation;

import com.ivancha.validation.impl.FreeNicknameValidator;
import jakarta.validation.Constraint;
import jakarta.validation.Payload;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;


@Constraint(validatedBy = FreeNicknameValidator.class)
@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
public @interface NicknameIsFree {

    String message() default "Это имя пользователя уже занято";

    Class<?>[] groups() default { };

    Class<? extends Payload>[] payload() default { };
}

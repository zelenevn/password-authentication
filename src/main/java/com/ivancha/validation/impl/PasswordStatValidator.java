package com.ivancha.validation.impl;

import com.ivancha.dto.PasswordStatContainer;
import com.ivancha.validation.PasswordStatMatches;
import jakarta.validation.ConstraintValidator;
import jakarta.validation.ConstraintValidatorContext;


public class PasswordStatValidator implements ConstraintValidator<PasswordStatMatches, PasswordStatContainer> {

    @Override
    public boolean isValid(PasswordStatContainer data, ConstraintValidatorContext context) {

        return (data.value().length() == data.keyPressTime().size()) &&
                (data.value().length() == (data.timeBetweenPresses().size() + 1));
    }
}

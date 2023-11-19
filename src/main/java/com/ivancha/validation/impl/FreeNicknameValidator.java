package com.ivancha.validation.impl;

import com.ivancha.repository.UserRepository;
import com.ivancha.validation.NicknameIsFree;
import jakarta.validation.ConstraintValidator;
import jakarta.validation.ConstraintValidatorContext;
import lombok.RequiredArgsConstructor;


@RequiredArgsConstructor
public class FreeNicknameValidator implements ConstraintValidator<NicknameIsFree, String> {

//    private final UserRepository userRepository;


    @Override
    public boolean isValid(String value, ConstraintValidatorContext context) {
//        return userRepository.findByNickname(value).isEmpty();
        // TODO: 19.11.2023 без ContextProvider я не смогу это сделать? (ну или жестко прописанных зависимостей)
        return true;  
    }
}

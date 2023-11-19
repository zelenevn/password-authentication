package com.ivancha.mapper;

import com.ivancha.dto.PasswordCreateDto;
import com.ivancha.entity.Password;
import com.ivancha.repository.UserRepository;
import lombok.RequiredArgsConstructor;


@RequiredArgsConstructor
public class PasswordCreateMapper implements Mapper<PasswordCreateDto, Password> {

    private final UserRepository userRepository;


    @Override
    public Password map(PasswordCreateDto object) {

        return Password.builder()
                .value(object.value())
                .timeBetweenPresses(object.timeBetweenPresses())
                .keyPressTime(object.keyPressTime())
                .user(userRepository.findById(object.userId())
                        .orElseThrow(() -> new RuntimeException("User с id, которому принадлежит пароль не существует")))
                .build();
    }
}

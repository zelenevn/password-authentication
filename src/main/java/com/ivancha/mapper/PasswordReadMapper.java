package com.ivancha.mapper;

import com.ivancha.dto.PasswordReadDto;
import com.ivancha.entity.Password;


public class PasswordReadMapper implements Mapper<Password, PasswordReadDto> {

    @Override
    public PasswordReadDto map(Password object) {
        return new PasswordReadDto(
                object.getId(),
                object.getValue(),
                object.getTimeBetweenPresses(),
                object.getKeyPressTime()
                );
    }
}

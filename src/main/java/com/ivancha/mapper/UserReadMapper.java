package com.ivancha.mapper;

import com.ivancha.dto.UserReadDto;
import com.ivancha.entity.User;
import lombok.RequiredArgsConstructor;


@RequiredArgsConstructor
public class UserReadMapper implements Mapper<User, UserReadDto> {

    private final PasswordReadMapper passwordReadMapper;


    @Override
    public UserReadDto map(User object) {
        return new UserReadDto(
                object.getId(),
                object.getNickname(),
                passwordReadMapper.map(object.getPassword())
        );
    }
}

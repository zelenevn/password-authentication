package com.ivancha.mapper;

import com.ivancha.dto.UserCreateDto;
import com.ivancha.entity.User;


public class UserCreateMapper implements Mapper<UserCreateDto, User> {

    @Override
    public User map(UserCreateDto object) {
        return User.builder()
                .nickname(object.nickname())
                .build();
    }
}

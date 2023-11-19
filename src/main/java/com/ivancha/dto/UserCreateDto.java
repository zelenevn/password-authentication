package com.ivancha.dto;

import com.ivancha.validation.NicknameIsFree;

public record UserCreateDto(
        @NicknameIsFree
        String nickname
){}

package com.ivancha.dto;

import com.ivancha.validation.PasswordStatMatches;
import com.ivancha.validation.UserExist;
import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.NotNull;

import java.util.Map;


@PasswordStatMatches
public record PasswordCreateDto(

        @NotEmpty
        String value,

        @NotNull
        @UserExist
        Integer userId,

        Map<Integer, Integer> timeBetweenPresses,
        Map<Integer, Integer> keyPressTime

) implements PasswordStatContainer { }

package com.ivancha.dto;

import java.util.Map;

public record PasswordReadDto(
        Integer id,
        String value,
        Map<Integer, Integer> timeBetweenPresses,
        Map<Integer, Integer> keyPressTime
)
{ }

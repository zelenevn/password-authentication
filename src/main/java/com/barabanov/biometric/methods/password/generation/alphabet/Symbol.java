package com.barabanov.biometric.methods.password.generation.alphabet;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;


@RequiredArgsConstructor
public enum Symbol implements Alphabet
{
    NUMBERS (Arrays.asList('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')),
    SPECIAL(Arrays.asList('.', '#', '?', '!', '¿', '¡', ':', ';', '%', '\'', '[', ']', '(', ')', '$', '&', '+', '-', '=', '~')),
    SPACE (Collections.singletonList(' '));

    @Getter
    private final List<Character> symbols;
}

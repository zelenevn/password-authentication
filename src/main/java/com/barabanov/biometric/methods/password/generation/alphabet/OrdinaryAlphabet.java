package com.barabanov.biometric.methods.password.generation.alphabet;


import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public enum OrdinaryAlphabet implements Alphabet
{
    LATIN_LOWERCASE(Arrays.asList('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')),
    LATIN_UPPERCASE(Arrays.asList('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')),
    CYRILLIC_LOWERCASE(Arrays.asList('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я')),
    CYRILLIC_UPPERCASE(Arrays.asList('А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я')),
    NUMBERS (Arrays.asList('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')),
    SPECIAL_SYM(Arrays.asList('.', '#', '?', '!', '¿', '¡', ':', ';', '%', '\'', '[', ']', '(', ')', '$', '&', '+', '-', '=', '~')),
    SPACE (Collections.singletonList(' '));


    private final List<Character> symbols;


    OrdinaryAlphabet(List<Character> symbols)
    {
        this.symbols = symbols;
    }

    @Override
    public List<Character> getSymbols()
    {
        return symbols;
    }
}

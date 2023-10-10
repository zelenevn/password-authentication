package com.ivancha.biometry.password;

import com.ivancha.biometry.alphabet.Alphabet;

import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.Collectors;


public class PasswordUtil
{

    public static String generate(Alphabet alphabet, int pswdLen)
    {
        if (alphabet.getLetters().isEmpty())
            return "";

        return ThreadLocalRandom.current().ints(pswdLen, 0, alphabet.getLetters().size())
                .mapToObj(alphabet.getLetters()::get)
                .map(Object::toString)
                .collect(Collectors.joining());
    }
}
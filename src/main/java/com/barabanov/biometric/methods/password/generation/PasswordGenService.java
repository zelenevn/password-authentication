package com.barabanov.biometric.methods.password.generation;

import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.Collectors;


@Service
public class PasswordGenService
{

    public String generate(List<Alphabet> alphabetSet, int pswdLen)
    {
        if (alphabetSet.isEmpty())
            return "";

        List<Character> combAlphabet = new ArrayList<>();

        for (Alphabet alphabet : alphabetSet)
            combAlphabet.addAll(alphabet.getSymbols());

        return ThreadLocalRandom.current().ints(pswdLen, 0, combAlphabet.size())
                .mapToObj(combAlphabet::get)
                .map(Object::toString)
                .collect(Collectors.joining());
    }
}

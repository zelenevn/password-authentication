package com.emelyanova.password.generation;

import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;

public class PasswordGenerator {

    public static String password(int l, List<Character> alphabet){
        return new Random().ints(l, 0, alphabet.size())
                .mapToObj(alphabet::get)
                .map(Object::toString)
                .collect(Collectors.joining());
    }
}

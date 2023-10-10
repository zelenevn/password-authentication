package com.ivancha.biometry.alphabet;

import java.util.ArrayList;
import java.util.List;


public class EmptyAbc implements Alphabet{

    private final List<Character> letters = new ArrayList<>();

    @Override
    public List<Character> getLetters() {
        return new ArrayList<>(letters);
    }
}

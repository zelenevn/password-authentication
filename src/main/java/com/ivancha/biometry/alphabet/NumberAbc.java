package com.ivancha.biometry.alphabet;

import java.util.List;


public class NumberAbc extends AlphabetDecorator {

    private final List<Character> letters = List.of('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');

    public NumberAbc(Alphabet alphabet) {
        super(alphabet);
    }

    @Override
    public List<Character> getLetters() {
        List<Character> mergedLetters = super.getLetters();
        mergedLetters.addAll(letters);
        return mergedLetters;
    }
}
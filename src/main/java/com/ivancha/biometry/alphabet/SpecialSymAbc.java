package com.ivancha.biometry.alphabet;

import java.util.List;


public class SpecialSymAbc extends AlphabetDecorator {

    private final List<Character> letters = List.of('.', '#', '?', '!', '¿', '¡', ':', ';', '%', '\'',
            '[', ']', '(', ')', '$', '&', '+', '-', '=', '~');

    public SpecialSymAbc(Alphabet alphabet) {
        super(alphabet);
    }

    @Override
    public List<Character> getLetters() {
        List<Character> mergedLetters = super.getLetters();
        mergedLetters.addAll(letters);
        return mergedLetters;
    }
}

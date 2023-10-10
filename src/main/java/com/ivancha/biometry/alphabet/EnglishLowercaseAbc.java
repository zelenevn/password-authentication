package com.ivancha.biometry.alphabet;

import java.util.List;


public class EnglishLowercaseAbc extends AlphabetDecorator{

    private final List<Character> letters = List.of('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z');

    public EnglishLowercaseAbc(Alphabet alphabet) {
        super(alphabet);
    }

    @Override
    public List<Character> getLetters() {
        List<Character> mergedLetters = super.getLetters();
        mergedLetters.addAll(letters);
        return mergedLetters;
    }
}

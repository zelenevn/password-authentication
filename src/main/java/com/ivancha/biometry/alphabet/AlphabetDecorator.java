package com.ivancha.biometry.alphabet;

import java.util.List;


public class AlphabetDecorator implements Alphabet{

    private final Alphabet alphabetImpl;

    public AlphabetDecorator(Alphabet alphabet) {
        this.alphabetImpl = alphabet;
    }

    @Override
    public List<Character> getLetters() {
        return alphabetImpl.getLetters();
    }
}

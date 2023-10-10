package com.ivancha.biometry.alphabet;

import java.util.List;


public class CyrillicUppercaseAbc extends AlphabetDecorator{

    private final List<Character> letters = List.of('А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К',
            'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я');

    public CyrillicUppercaseAbc(Alphabet alphabet) {
        super(alphabet);
    }

    @Override
    public List<Character> getLetters() {
        var mergedLetters = super.getLetters();
        mergedLetters.addAll(letters);
        return mergedLetters;
    }
}

package com.ivancha.biometry.alphabet;

import java.util.List;


public class CyrillicLowercaseAbc extends AlphabetDecorator{

    private final List<Character> letters = List.of('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к',
            'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я');

    public CyrillicLowercaseAbc(Alphabet alphabet) {
        super(alphabet);
    }

    @Override
    public List<Character> getLetters() {
        var mergedLetters = super.getLetters();
        mergedLetters.addAll(letters);
        return mergedLetters;
    }
}

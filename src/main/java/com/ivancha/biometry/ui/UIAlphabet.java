package com.ivancha.biometry.ui;


import com.ivancha.biometry.alphabet.*;

import java.util.Objects;

enum UIAlphabet {
    LATIN_LOWERCASE(1, EnglishLowercaseAbc.class),
    LATIN_UPPERCASE(2, EnglishUppercaseAbc.class),
    NUMBERS(3, NumberAbc.class),
    SPECIAL_SYM(4, SpecialSymAbc.class),
    CYRILLIC_LOWERCASE(5, CyrillicLowercaseAbc.class),
    CYRILLIC_UPPERCASE(6, CyrillicUppercaseAbc.class);

    private final int alias;
    private final Class<?> implClass;

    UIAlphabet(int alias, Class<?> implClass) {
        this.alias = alias;
        this.implClass = Objects.requireNonNull(implClass);
    }

    static UIAlphabet fromAlias(int alias){
        for (UIAlphabet alphabet : UIAlphabet.values())
            if (alphabet.alias == alias)
                return alphabet;

        return null;
    }

    public int getAlias() {
        return alias;
    }

    public Class<?> getImplClass() {
        return implClass;
    }
}

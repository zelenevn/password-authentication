package com.ivancha.biometry.ui;

import com.ivancha.biometry.alphabet.Alphabet;
import com.ivancha.biometry.alphabet.EmptyAbc;

import java.lang.reflect.InvocationTargetException;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;


public class UiUtil {

    public static Alphabet createAlphabetByAliases(List<Integer> aliases) throws NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {

        return createByAliasesRecHelper(new LinkedList<>(aliases), null);
    }


    @SuppressWarnings("ConstantConditions")
    private static Alphabet createByAliasesRecHelper(Queue<Integer> aliases, Alphabet alphabet) throws NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {
        if (alphabet == null)
            alphabet = new EmptyAbc();

        if (aliases.isEmpty())
            return alphabet;

        // подавляем may produce NullPointer getImplClass()
        // т.к. при создании объекта Alphabet есть проверка на null этого поля
        return (Alphabet) UIAlphabet.fromAlias(aliases.poll())
                .getImplClass()
                .getDeclaredConstructor(Alphabet.class)
                .newInstance(createByAliasesRecHelper(aliases, alphabet));

    }
}

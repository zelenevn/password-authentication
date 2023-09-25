package com.barabanov.biometric.methods.service;

import com.barabanov.biometric.methods.password.generation.alphabet.Alphabet;
import org.reflections.Reflections;
import org.springframework.stereotype.Service;

import java.util.*;


@Service
public class AlphabetService
{

    private static final Map<String, Alphabet> alpbtNameToAlpbt = new HashMap<>();


    static {
        loadAlphabets();
    }


    public List<Alphabet> determineAlphabets(List<String> alphabetNames)
    {
        List<Alphabet> alphabets = new ArrayList<>();
        for (String name : alphabetNames)
        {
            if (alpbtNameToAlpbt.containsKey(name))
                alphabets.add(alpbtNameToAlpbt.get(name));
        }

        return alphabets;
    }


    private static void loadAlphabets()
    {
        Reflections reflections = new Reflections(Alphabet.class.getPackage().getName());

        Set<Class<? extends Alphabet>> subTypesOfAlphabet = reflections.getSubTypesOf(Alphabet.class);

        for (Class<? extends Alphabet> alphabetClass : subTypesOfAlphabet)
        {
            if(alphabetClass.isEnum())
                for (Alphabet alphabet : alphabetClass.getEnumConstants())
                    alpbtNameToAlpbt.put(alphabet.toString(), alphabet);
        }

    }
}

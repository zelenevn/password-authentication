package com.barabanov.biometric.methods.service;

import com.barabanov.biometric.methods.password.generation.alphabet.Alphabet;
import org.reflections.Reflections;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.stream.Collectors;


@Service
public class AlphabetService
{
    private static final String SEP = ".";

    // Alphabet name is name_of_enum + sep +name_of_constant
    private static final Map<String, Alphabet> alpbtNameToAlpbt = new HashMap<>();

    private static final Map<String, List<Alphabet>> groupToAlphabets = new HashMap<>();


    static {
        loadAlphabets();
    }


    public List<Alphabet> determineAlphabets(Map<String, List<String>> alphabetNames)
    {
        List<Alphabet> alphabets = new ArrayList<>();
        for (Map.Entry<String, List<String>> entry : alphabetNames.entrySet())
        {
            for (String alphabetLastName : entry.getValue())
            {
                String alphabetName = entry.getKey().toLowerCase() + SEP + alphabetLastName.toLowerCase();
                if (alpbtNameToAlpbt.containsKey(alphabetName))
                    alphabets.add(alpbtNameToAlpbt.get(alphabetName));
            }
        }

        return alphabets;
    }


    public List<String> getGroups()
    {
        return new ArrayList<>(groupToAlphabets.keySet());
    }


    public List<String> getAlphabetSimpleNames(String group)
    {
        return groupToAlphabets.get(group.toLowerCase()).stream()
                .map(alphabet -> alphabet.toString().toLowerCase())
                .collect(Collectors.toList());
    }


    private static void loadAlphabets()
    {
        Reflections reflections = new Reflections(Alphabet.class.getPackage().getName());

        Set<Class<? extends Alphabet>> subTypesOfAlphabet = reflections.getSubTypesOf(Alphabet.class);


        for (Class<? extends Alphabet> alphabetClass : subTypesOfAlphabet)
        {
            List<Alphabet> alphabets = new ArrayList<>();
            String alphabetGroup = alphabetClass.getSimpleName().toLowerCase();
            if(alphabetClass.isEnum())
            {
                for (Alphabet alphabet : alphabetClass.getEnumConstants())
                {
                    alphabets.add(alphabet);
                    alpbtNameToAlpbt.put(alphabetGroup + SEP + alphabet.toString().toLowerCase(), alphabet);
                }
            }

            groupToAlphabets.put(alphabetGroup, alphabets);
        }
    }

}

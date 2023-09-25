package com.barabanov.biometric.methods.password.generation;

import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;


@Service
public class PasswordGenService
{

    public char[] generate(List<Alphabet> alphabetSet, int pswdLen)
    {
        if (alphabetSet.isEmpty())
            return new char[0];

        List<Character> combAlphabet = new ArrayList<>();
        for (Alphabet alphabet : alphabetSet)
            combAlphabet.addAll(alphabet.getSymbols());
        
        char[] password = new char[pswdLen];
        for (int i = 0; i < pswdLen; i++)
            password[i] = combAlphabet.get(ThreadLocalRandom.current().nextInt(0, combAlphabet.size()));

        return password;
    }


    public void erasePswd(char[] pswd)
    {
        Arrays.fill(pswd, (char) 0);
    }
}

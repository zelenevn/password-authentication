package com.barabanov.biometric.methods.password.generation.alphabet;

import java.util.List;

// The implementation must be an enum.
// Also, the implementation enum must be in the same package as this interface.
public interface Alphabet
{
    List<Character> getSymbols();
}

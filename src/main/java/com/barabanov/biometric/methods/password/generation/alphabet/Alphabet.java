package com.barabanov.biometric.methods.password.generation.alphabet;

import java.util.List;

// Must be an enum and its objects must have unique names among all objects of this interface.
// Also, the implementation enumeration must be in the same package as this interface.
public interface Alphabet
{
    List<Character> getSymbols();
}

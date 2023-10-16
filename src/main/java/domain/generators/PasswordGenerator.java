package domain.generators;

import domain.models.Alphabet;

public interface PasswordGenerator {

    String generatePassword(int length, Alphabet alphabet);

    boolean containNumbers(String password);

    boolean containUpperCase(String password);

    boolean containPunctuationMarks(String password);
}

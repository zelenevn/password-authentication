package groupId.generators;

import groupId.Alphabet;

public interface PasswordGenerator {

    String generatePassword(int length, Alphabet alphabet);

    boolean containNumbers(String password);

    boolean containUpperCase(String password);

    boolean containPunctuationMarks(String password);
}

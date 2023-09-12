package domain;

public interface PasswordGenerator {
    String generatePassword(int length, boolean numbers, boolean punctuationMarks, boolean upperCase);
}

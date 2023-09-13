package domain;

public interface PasswordBuilder {
    String generatePassword(int length, boolean numbers, boolean punctuationMarks, boolean upperCase);
}

package domain;

public interface PasswordController {
    String generatePassword(int length, boolean numbers, boolean punctuationMarks, boolean upperCase);
}

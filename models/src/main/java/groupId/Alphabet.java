package groupId;

public interface Alphabet {
    StringBuilder getSymbols();
    void addUpperCase(boolean upperCase);
    void addPunctuationMarks(boolean punctuationMarks);
    void addNumbers(boolean numbers);
}

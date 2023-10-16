package domain.models;

public class Alphabet {

    private final StringBuilder alphabet = new StringBuilder();

    public Alphabet() {
    }

    public void addUpperCase(boolean upperCase) {
        if (upperCase) {
            alphabet.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
        }
    }

    public void addPunctuationMarks(boolean punctuation) {
        if (punctuation) {
            alphabet.append("./?><!^");
        }
    }

    public void addNumbers(boolean numbers){
        if (numbers){
            alphabet.append("0123456789");
        }
    }

    public StringBuilder getSymbols() {
        return alphabet.append("abcdefghijklmnopqrstuvwxyz");
    }
}

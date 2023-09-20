package groupId;

public class GermanAlphabet extends EnglishAlphabet {
    private final StringBuilder alphabet;

    public GermanAlphabet(Alphabet alphabet) {
        this.alphabet = alphabet.getSymbols();
    }

    @Override
    public void addUpperCase(boolean upperCase) {
        if (upperCase) {
            alphabet.append("ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß");
        }
    }

    @Override
    public void addPunctuationMarks(boolean punctuation) {
        if (punctuation) {
            alphabet.append("./?><!^");
        }
    }

    @Override
    public void addNumbers(boolean numbers){
        if (numbers){
            alphabet.append("0123456789");
        }
    }

    @Override
    public StringBuilder getSymbols() {
        return alphabet.append("abcdefghijklmnopqrstuvwxyzäöüß");
    }
}

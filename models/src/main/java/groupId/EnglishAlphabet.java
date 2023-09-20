package groupId;

public class EnglishAlphabet implements Alphabet {
    private StringBuilder alphabet = new StringBuilder();

    public EnglishAlphabet(StringBuilder alphabet) {
        this.alphabet = alphabet;
    }

    public EnglishAlphabet() {
    }

    @Override
    public void addUpperCase(boolean upperCase) {
        if (upperCase) {
            alphabet.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
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
        return alphabet.append("abcdefghijklmnopqrstuvwxyz");
    }
}

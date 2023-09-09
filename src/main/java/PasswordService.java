import java.security.SecureRandom;

public class PasswordService {
    private StringBuilder alphabet;
    private SecureRandom secureRandom = new SecureRandom();
    private StringBuilder password;

    public String generatePassword(int length, boolean numbers,
                                   boolean punctuationMarks, boolean upperCase) {
        password = new StringBuilder();
        alphabet = new StringBuilder();

        alphabet.append("abcdefghijklmnopqrstuvwxyz");
        if (numbers) {
            alphabet.append("0123456789");
        }
        if (punctuationMarks) {
            alphabet.append("./?><!^");
        }
        if (upperCase) {
            alphabet.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
        }

        StringBuilder replay = new StringBuilder();
        for (int i = 0; i < length; i++) {
            int randomIndex = secureRandom.nextInt(alphabet.length());
            if (!replay.toString().contains(Integer.toString(randomIndex))) {
                password.append(alphabet.charAt(randomIndex));
                replay.append(randomIndex);
            } else {
                length++;
            }
        }
        return password.toString();
    }
}

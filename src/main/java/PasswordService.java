import java.security.SecureRandom;

/**
 * Класс для работы с паролями
 *
 * @autor Pycukvsu
 */
public class PasswordService {
    private StringBuilder alphabet;
    private final SecureRandom secureRandom = new SecureRandom();
    private StringBuilder password;

    /**
     * Метод генерирует рандомные пароли.
     * Также метод обрабатывает то, чтобы символы пароля не повторялись.
     * Заданая длина пароля не может быть больше длины алфавита.
     *
     * @param length - длина пароля
     * @param numbers - будет ли пароль содержать цифры
     * @param punctuationMarks - будет ли содержать пароль специальные символы
     * @param upperCase - будет ли пароль содержать буквы верхнего регистра
     *
     * @return password - получившийся пароль
     */
    public String generatePassword(int length, boolean numbers,
                                   boolean punctuationMarks, boolean upperCase) {
        password = new StringBuilder();
        alphabet = new StringBuilder();

        // Добавление в алфавит сиволов
        // Нижний регистр по дефолту добавляется
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

        if (length > alphabet.length()){
            return "Уменьшите длину пароля";
        }

        // Обработка повторяющихся символов
        // Индексы сохраняются в replay
        StringBuilder replay = new StringBuilder();
        for (int i = 0; i < length; i++) {
            int randomIndex = secureRandom.nextInt(alphabet.length());

            // Если randomIndex не содержится в replay
            // то добавляем по этому индексу символ из alphabet в password
            // и добавляем randomIndex в replay
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

package domain;

import java.security.SecureRandom;

/**
 * Класс для работы с паролями
 *
 * @autor Pycukvsu
 */
public class PasswordGenerator implements PasswordBuilder {
    private final SecureRandom secureRandom = new SecureRandom();

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
    @Override
    public String generatePassword(int length, boolean numbers,
                                   boolean punctuationMarks, boolean upperCase) {
        StringBuilder alphabet = new StringBuilder();
        byte[] password = new byte[length];

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
            return "Укажите длину поменьше";
        }

        // Обработка повторяющихся символов
        // Индексы сохраняются в replay
        int lastIndex = 0;
        StringBuilder replay = new StringBuilder();
        for (int i = 0; i < length; i++) {
            int randomIndex = secureRandom.nextInt(alphabet.length());

            // Если randomIndex не содержится в replay
            // то добавляем по этому индексу символ из alphabet в password
            // и добавляем randomIndex в replay
            if (!replay.toString().contains(Integer.toString(randomIndex))) {
                password[lastIndex] = (byte) alphabet.charAt(randomIndex);
                replay.append(randomIndex);
                lastIndex++;
            } else {
                length++;
            }
        }
        return new String(password);
    }
}

package domain.generators;

import domain.models.Alphabet;

import java.security.SecureRandom;
import java.util.HashSet;
import java.util.Set;

/**
 * Класс для работы с паролями
 */
public class PasswordGeneratorImpl implements PasswordGenerator {
    private final SecureRandom secureRandom = new SecureRandom();
    private Set<Integer> replayIndex;

    /**
     * Метод генерирует рандомные пароли.
     * Также метод обрабатывает то, чтобы символы пароля не повторялись.
     * Заданая длина пароля не может быть больше длины алфавита.
     *
     * @param length - длина пароля
     * @return password - получившийся пароль
     */
    @Override
    public String generatePassword(int length, Alphabet symbols) {
        StringBuilder alphabet = symbols.getSymbols();
        byte[] password = new byte[length];
        replayIndex = new HashSet<>();

        if (length > alphabet.length()){
            return "Укажите длину поменьше";
        }

        // Обработка повторяющихся символов
        // Индексы сохраняются в replay
        int lastIndex = 0;
        for (int i = 0; i < length; i++) {
            int randomIndex = secureRandom.nextInt(alphabet.length());

            // Если randomIndex не содержится в replay
            // то добавляем по этому индексу символ из alphabet в password
            // и добавляем randomIndex в replay
            if (!viewReplays(randomIndex)) {
                password[lastIndex] = (byte) alphabet.charAt(randomIndex);
                lastIndex++;
            } else {
                length++;
            }
        }

        return new String(password);
    }

    /**
     * Метод проверяет наличие повторных индексов.
     *
     * @param index - индекс элемента
     * @return  false - такой элемент есть | true - такого элемента нет
     */
    private boolean viewReplays(int index){
        int lastSize = replayIndex.size();
        replayIndex.add(index);
        return replayIndex.size() != lastSize + 1;
    }

    /**
     * Метод проверяет наличие цифр в пароле.
     *
     * @param password - пароль
     * @return  false - цифр в пароле нет | true - цифры в пароле есть
     */
    @Override
    public boolean containNumbers(String password){
        for (int i = 48; i < 58; i++) {
            char number = (char) i;
            if (password.contains(String.valueOf(number))){
                return true;
            }
        }

        return false;
    }

    /**
     * Метод проверяет наличие букв верхнего регистра в пароле.
     *
     * @param password - пароль
     * @return false - буквы верхнего регистра в пароле нет | true - буквы верхнего регистра в пароле есть
     */
    @Override
    public boolean containUpperCase(String password){
        for (int i = 65; i < 91; i++) {
            char number = (char) i;
            if (password.contains(String.valueOf(number))){
                return true;
            }
        }

        return false;
    }

    /**
     * Метод проверяет наличие специальных символов в пароле.
     *
     * @param password - пароль
     * @return false - специальных символов в пароле нет | true - специальные символы в пароле есть
     */
    @Override
    public boolean containPunctuationMarks(String password){
        for (int i = 33; i < 48; i++) {
            char number = (char) i;
            if (password.contains(String.valueOf(number))){
                return true;
            }
        }

        return false;
    }
}

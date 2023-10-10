package com.ivancha.biometry.ui;

import com.ivancha.biometry.math.MathUtil;
import com.ivancha.biometry.password.PasswordUtil;
import org.bouncycastle.crypto.digests.MD5Digest;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.util.encoders.Hex;

import java.lang.reflect.InvocationTargetException;
import java.security.Security;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;


public class ConsoleUI {

    public static void main(String[] args) throws InvocationTargetException, NoSuchMethodException, InstantiationException, IllegalAccessException {

        System.out.println("""
                Выберите из чего будет состоять алфавит для генерации пароля
                1 - Latin lowercase
                2 - Latin uppercase
                3 - Numbers
                4 - Special symbols
                5 - Cyrillic lowercase
                6 - Cyrillic uppercase""");

        var scanner = new Scanner(System.in);
        var aliasesCombination = scanner.nextLine();
        var aliases = Arrays.stream(aliasesCombination.trim().split("\s*,\s*")).map(Integer::parseInt).toList();
        var alphabet = UiUtil.createAlphabetByAliases(aliases);

        System.out.println("Введите число символов в пароле");
        var password = PasswordUtil.generate(alphabet, scanner.nextInt());
        scanner.nextLine();

        Security.addProvider(new BouncyCastleProvider());

        System.out.println("Пароль: " + password);
        System.out.println("\nНаберите пароль");
        var speedOfEntering = measureSpeedOfEntering(scanner, password);
        System.out.println("MD5: " + MD5(password));
        System.out.printf("Дисперсия: %.2f %s\n", MathUtil.dispersion(speedOfEntering), " мс");
        System.out.printf("Математическое ожидание: %.2f %s\n", MathUtil.mathExpectedVal(speedOfEntering), " мс");
    }


    private static String MD5(String password) {
        byte[] passwordBytes = password.getBytes();

        MD5Digest example = new MD5Digest();
        example.update(passwordBytes, 0, passwordBytes.length);

        byte[] digested = new byte[new MD5Digest().getDigestSize()];
        example.doFinal(digested, 0);

        return new String(Hex.encode(digested));
    }


    private static List<Long> measureSpeedOfEntering(Scanner scanner, String word){

        List<Long> time = new LinkedList<>();
        for (char s : word.toCharArray()){
            var start = System.currentTimeMillis();
            scanner.nextLine();
            time.add(System.currentTimeMillis() - start);
        }

        return time;
    }

}


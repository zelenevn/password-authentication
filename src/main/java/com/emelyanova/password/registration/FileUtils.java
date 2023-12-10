package com.emelyanova.password.registration;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class FileUtils {

    public static List<Character> readAlphabet(String file_name){
        try (BufferedReader reader = new BufferedReader(
                new FileReader("src/main/resources/alphabet/" + file_name))){

            String[] chars = reader.readLine().split("\s+");
            List<Character> alphabet = new ArrayList<>();
            for (String s : chars)
                alphabet.add(s.toCharArray()[0]);

            return alphabet;

        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static List<String> fileNames(String combination){
        String[] fileAliases = combination.split("\s*,\s*");
        int[] number = new int[fileAliases.length];
        for (int i = 0; i < fileAliases.length; i++) {
            number[i] = Integer.parseInt(fileAliases[i]);
        }
        List<String> fileNames = new ArrayList<>();
        for (int i = 0; i < number.length; i++){
            switch (number[i])
            {
                case 1:
                {
                    fileNames.add("lower_case.txt");
                    break;
                }
                case 2:
                {
                    fileNames.add("upper_case.txt");
                    break;
                }
                case 3:
                {
                    fileNames.add("numbers.txt");
                    break;
                }
                case 4:
                {
                    fileNames.add("special_symbols.txt");
                    break;
                }
            }
        }
        return fileNames;
    }
}

package com.emelyanova.password.registration;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;

public class ConsoleUI {

    public static void main(String[] args) {

        String url = "jdbc:postgresql://localhost/Registration";
        String username = "postgres";
        String password = "35728534oe";
        try {
            Class.forName("org.postgresql.Driver").getDeclaredConstructor().newInstance();
            Connection conn = DriverManager.getConnection(url, username, password);

            Scanner scan = new Scanner(System.in);

            while (true) {

                System.out.println("""
                        Введите команду:\s
                        1 - Зарегистрировать пользователя
                        2 - Показать всех зарегистрированных пользователей
                        3 - завершение работы""");

                String userChoice = scan.nextLine();
                if (userChoice.equals("1")) {
                    registerNewUser(scan);
                }
                if (userChoice.equals("2")){
                    chowAllUsers(conn);
                }
                if (userChoice.equals("3")){
                    break;
                }
            }
            conn.close();
        } catch (Exception ex) {
            System.out.println("Подключение сорвалось :(... " + ex);
        }

    }

    private static void registerNewUser(Scanner scanner) {
        System.out.println("Введите логин:");
        String login = scanner.nextLine();
        //scan.nextLine();

        int l = 8;
        String combinationAlphabet = "1, 2, 3";
        List<String> fileNames = FileUtils.fileNames(combinationAlphabet);
        List<Character> alphabet = new ArrayList<>();
        for (String s: fileNames){
            alphabet.addAll(Objects.requireNonNull(FileUtils.readAlphabet(s)));
        }

        String password = PasswordGenerator.password(l, alphabet);
        System.out.println("Ваш пароль: " + password);

        List<Long> time_between_presses = new ArrayList<>();
        List<Long>  key_press_time = new ArrayList<>();
        /*
        List<Long> inputDuration = new ArrayList<>();
        for (int i = 0; i < l; i++){
            long start = System.currentTimeMillis();
            scanner.nextLine();
            long end = System.currentTimeMillis();
            inputDuration.add(end - start);
        }
         */
    }

    private static void chowAllUsers(Connection connection)
    {
        try (PreparedStatement statement = connection.prepareStatement("""
                SELECT nickname, p.value password, time_between_presses, key_press_time
                FROM users u
                INNER JOIN password p
                ON u.nickname = p.user_nickname
                INNER JOIN metric m
                ON (p.user_nickname = m.user_nickname AND p.value = m.value);
                """)) {
            try (ResultSet resultSet = statement.executeQuery())
            {
                resultSet.next();
                String nickname = resultSet.getString("nickname");
                String password = resultSet.getString("password");
                String timeBetweenPresses = resultSet.getString("time_between_presses");
                String keyPressTime = resultSet.getString("key_press_time");

                System.out.printf("%s - пароль: %s; время между нажатиями клавиш: %s; время нажатия клавиш: %s",
                        nickname, password, timeBetweenPresses, keyPressTime);
            }
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
    }

}

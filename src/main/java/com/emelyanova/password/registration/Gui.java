package com.emelyanova.password.registration;

import net.miginfocom.swing.MigLayout;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

class Gui {

    public static void main(String args[]) {

        JFrame frame = new JFrame("Пароли, парольчики, паролища");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 400);

        JPanel regPanel = new JPanel(new MigLayout());

        JLabel registerLbl = new JLabel("Зарегистрируемся");
        regPanel.add(registerLbl, "span");

        JLabel usernameLbl = new JLabel("Введите имя пользователя");
        JTextField usernameTextField = new JTextField(25);
        regPanel.add(usernameLbl);
        regPanel.add(usernameTextField, "wrap");

        final String[] password = {generatePassword()};

        JLabel passwordLbl = new JLabel("Запомните и введите пароль: " + password[0]);
        regPanel.add(passwordLbl);
        JTextField passwordTextField = new JTextField(10); // принимает до 20 символов
        KeyStatisticsCollector keyStatistics = new KeyStatisticsCollector();
        passwordTextField.addKeyListener(keyStatistics);
        regPanel.add(passwordTextField);

        JButton replaceBtn = new JButton("Заменить пароль");
        replaceBtn.addActionListener(new AbstractAction() {
            @Override
            public void actionPerformed(ActionEvent e) {
                password[0] = generatePassword();
                passwordLbl.setText("Запомните и введите пароль: " + password[0]);
            }
        });
        regPanel.add(replaceBtn, "wrap");

        JButton sendBtn = new JButton("Отправить");
        sendBtn.addActionListener(new AbstractAction() {

            @Override
            public void actionPerformed(ActionEvent e) {

                String userEnteredPassword = passwordTextField.getText();
                if (!userEnteredPassword.equals(password[0])) {

                    JLabel passwordDontMatchLbl = new JLabel("Введёный вами пароль не совпадает с предоставленным");
                    regPanel.add(passwordDontMatchLbl, "wrap");

                    JButton okBtn = new JButton("покорно введу ещё раз");
                    okBtn.addActionListener(new AbstractAction() {
                        @Override
                        public void actionPerformed(ActionEvent e) {
                            passwordTextField.setText("");
                            regPanel.remove(passwordDontMatchLbl);
                            regPanel.remove(okBtn);
                            regPanel.repaint();
                        }
                    });
                    regPanel.add(okBtn, "wrap");
                    regPanel.revalidate();
                    regPanel.repaint();
                }
                else {

                    List<Long> timeBetweenPresses = keyStatistics.getTimeBetweenPresses();
                    timeBetweenPresses.remove(0);

                    registerNewUser(
                            usernameTextField.getText(),
                            password[0],
                            timeBetweenPresses,
                            keyStatistics.getPressTimeList());

                    usernameTextField.setText("");
                    passwordTextField.setText("");
                }
            }
        });
        regPanel.add(sendBtn, "span");

        JButton showAllUsersBtn = new JButton("Показать всех зарегистрированных пользователей");
        showAllUsersBtn.addActionListener(new AbstractAction() {
            @Override
            public void actionPerformed(ActionEvent e) {

                StringBuilder sb = new StringBuilder();
                List<UserInfoReadDto> userInfoList = getAllUsers();

                for(int i = 0; i < userInfoList.size(); i++) {

                    UserInfoReadDto userDto = userInfoList.get(i);
                    sb.append(i).append(": ");
                    sb.append("   Имя пользователя: ").append(userDto.getNickname());
                    sb.append("   Пароль:").append(userDto.getPassword());
                    sb.append("   Время нажатия клавиш: ").append(userDto.getKeyPressTime());
                    sb.append("   Время между нажатиями клавиш: ").append(userDto.getTimeBetweenPresses());
                    sb.append("\n");
                }
                JOptionPane.showMessageDialog(regPanel, sb.toString());
            }
        });
        regPanel.add(showAllUsersBtn, "span");

        frame.getContentPane().add(regPanel);
        frame.setVisible(true);
    }


    private static void registerNewUser(String username, String password, List<Long> timeBetweenPresses, List<Long> pressTimeList) {
        try {
            try (PreparedStatement statement = Connect.getConnection().prepareStatement("""
                    INSERT INTO users(nickname)
                    VALUES (?)
                    """)) {
                statement.setString(1, username);

                statement.execute();
            }
            try (PreparedStatement statement = Connect.getConnection().prepareStatement("""
                    INSERT INTO password(user_nickname, value)
                    VALUES (?, ?)
                    """)) {
                statement.setString(1, username);
                statement.setString(2, password);

                statement.execute();
            }
            try (PreparedStatement statement = Connect.getConnection().prepareStatement("""
                    INSERT INTO metric(user_nickname, value, time_between_presses, key_press_time)
                    VALUES (?, ?, ?, ?)
                    """)) {
                statement.setString(1, username);
                statement.setString(2, password);
                statement.setString(3,
                        timeBetweenPresses.stream()
                        .map(Object::toString)
                        .collect(Collectors.joining(",")));
                statement.setString(4,
                        pressTimeList.stream()
                        .map(Object::toString)
                        .collect(Collectors.joining(",")));

                statement.execute();
            }
        }
        catch (SQLException e) {
            throw new RuntimeException(e);
        }

    }


    private static List<UserInfoReadDto> getAllUsers() {
        try (PreparedStatement statement = Connect.getConnection().prepareStatement("""
                SELECT nickname, p.value password, time_between_presses, key_press_time
                FROM users u
                INNER JOIN password p
                ON u.nickname = p.user_nickname
                INNER JOIN metric m
                ON (p.user_nickname = m.user_nickname AND p.value = m.value);
                """);
             ResultSet resultSet = statement.executeQuery()){

            List<UserInfoReadDto> userInfoList = new ArrayList<>();
            while (resultSet.next())
                userInfoList.add(new UserInfoReadDto(
                        resultSet.getString("nickname"),
                        resultSet.getString("password"),
                        resultSet.getString("time_between_presses"),
                        resultSet.getString("key_press_time")));

            return userInfoList;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }


    private static String generatePassword() {
        int l = 8;
        String combinationAlphabet = "1, 2, 3";
        List<String> fileNames = FileUtils.fileNames(combinationAlphabet);
        List<Character> alphabet = new ArrayList<>();
        for (String s: fileNames){
            alphabet.addAll(Objects.requireNonNull(FileUtils.readAlphabet(s)));
        }

        return PasswordGenerator.password(l, alphabet);
    }


    private static class UserInfoReadDto
    {
        private final String nickname;
        private final String password;
        private final String timeBetweenPresses;
        private final String keyPressTime;

        UserInfoReadDto(String nickname, String password, String timeBetweenPresses, String keyPressTime) {
            this.nickname = nickname;
            this.password = password;
            this.timeBetweenPresses = timeBetweenPresses;
            this.keyPressTime = keyPressTime;
        }

        public String getNickname() {
            return nickname;
        }

        public String getPassword() {
            return password;
        }

        public String getTimeBetweenPresses() {
            return timeBetweenPresses;
        }

        public String getKeyPressTime() {
            return keyPressTime;
        }
    }



    private static class KeyStatisticsCollector implements KeyListener {

        private final List<Long> timeBetweenPresses = new ArrayList<>();
        private final List<Long> pressTimeList = new ArrayList<>();

        private boolean isKeyPressed = false;
        private long startPressFreeTime = System.currentTimeMillis();
        private long startPressTime;

        public void keyTyped(KeyEvent e) {

            if (!isKeyPressed) {

                long nowTime = System.currentTimeMillis();

                startPressTime = nowTime;
                timeBetweenPresses.add(nowTime - startPressFreeTime);
                isKeyPressed = true;
            }
        }

        public void keyReleased(KeyEvent e) {

            if (isKeyPressed) {

                long nowTime = System.currentTimeMillis();

                pressTimeList.add(nowTime - startPressTime);
                startPressFreeTime = nowTime;
                isKeyPressed = false;
            }
        }

        public void keyPressed(KeyEvent e) {}

        public List<Long> getTimeBetweenPresses() { return timeBetweenPresses; }

        public List<Long> getPressTimeList() { return pressTimeList; }
    }
}

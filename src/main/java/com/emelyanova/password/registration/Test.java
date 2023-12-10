package com.emelyanova.password.registration;


import java.sql.SQLException;
import java.sql.Statement;
import java.util.List;

public class Test {

    public static void main(String[] args) {
       fillingTheDatabase("Oksana1", "dfghjkl", List.of(1,2,3,4), List.of(1,2,3,4));
    }

    public static void fillingTheDatabase(String login,String password, List<Integer> time_between_presses, List<Integer>  key_press_time) {
        try {
            System.out.println("Connection to Store DB succesfull!");
            Statement statement =  Connect.getConnection().createStatement();
            statement.executeUpdate(String.format("INSERT INTO users(nickname) VALUES ('%s')", login));
            statement.executeUpdate(String.format("INSERT INTO password(user_nickname, value ) VALUES ('%s', '%s')", login, password));
            statement.executeUpdate(String.format("INSERT INTO metric(user_nickname, value, time_between_presses, key_press_time) VALUES ('%s', '%s', '%s', '%s')", login, password, time_between_presses, key_press_time));
        }
        catch (SQLException throwables) {
            throwables.printStackTrace();
        }
    }
}

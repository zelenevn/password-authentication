package com.emelyanova.password.registration;

import java.sql.Connection;
import java.sql.DriverManager;

public class Connect {
    private static String url = "jdbc:postgresql://localhost/Registration";
    private static String username = "postgres";
    private static String password = "35728534oe";

    public static Connection getConnection() {
        try {
            Class.forName("org.postgresql.Driver").getDeclaredConstructor().newInstance();
            return DriverManager.getConnection(url, username, password);
        } catch (Exception ex) {
            System.out.println("Connection failed... " + ex);
            return null;
        }
    }

}

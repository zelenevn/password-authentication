package com.ivancha.util;

import lombok.experimental.UtilityClass;
import org.hibernate.SessionFactory;
import org.testcontainers.containers.PostgreSQLContainer;


@UtilityClass
public class HibernateTestUtil {

    private static final PostgreSQLContainer postgres = new PostgreSQLContainer<>("postgres:16.1");

    static {
        postgres.start();
    }


    public static SessionFactory buildSessionFactory() {

        var configuration = HibernateUtil.buildConfiguration();
        configuration.setProperty("hibernate.connection.url", postgres.getJdbcUrl());
        configuration.setProperty("hibernate.connection.username", postgres.getUsername());
        configuration.setProperty("hibernate.connection.password", postgres.getPassword());
        configuration.configure();

        return configuration.buildSessionFactory();
    }
}

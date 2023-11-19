package com.ivancha.util;

import com.ivancha.entity.Password;
import com.ivancha.entity.User;
import lombok.experimental.UtilityClass;
import org.hibernate.Session;

import java.util.Map;

@UtilityClass
public class TestDataImporter {

    public void importData(Session session) {

        session.beginTransaction();

        var dima = saveUser(session, "Dima");
        var vova = saveUser(session, "Vova");
        var andrey = saveUser(session, "Andrey");
        var petya = saveUser(session, "Petya");
        var iliya = saveUser(session, "Iliya");

        var dimaPassword = savePassword(
                session,
                "pass",
                dima,
                Map.of(1, 12, 2, 13, 3, 14),
                Map.of(1, 4, 2, 5, 3, 8, 4, 2));
        var vovaPassword = savePassword(
                session,
                "1234",
                vova, Map.of(1, 4, 2, 4, 3, 4),
                Map.of(1, 4, 2, 4, 3, 4, 4, 4)
        );
        var andreyPassword = savePassword(
                session,
                "qwerty",
                andrey,
                Map.of(1, 11, 2, 12, 3, 13, 4, 10, 5, 12),
                Map.of(1, 4, 2, 8, 3, 5, 4, 5, 5, 6, 6, 5));
        var petyaPassword = savePassword(
                session,
                "1W43yM",
                petya,
                Map.of(1, 25, 2, 63, 3, 71, 4, 23, 5, 48),
                Map.of(1, 12, 2, 18, 3, 21, 4, 34, 5, 56, 6, 12));

        session.getTransaction().commit();
    }


    private static Password savePassword(Session session,
                                         String pass,
                                         User user,
                                         Map<Integer, Integer> timeBetweenPresses,
                                         Map<Integer, Integer> keyPressTime) {

        var password = Password.builder()
                .value(pass)
                .user(user)
                .timeBetweenPresses(timeBetweenPresses)
                .keyPressTime(keyPressTime)
                .build();

        session.persist(password);

        return password;
    }


    private static User saveUser(Session session, String nickname) {

        var user = User.builder()
                .nickname(nickname)
                .build();

        session.persist(user);

        return user;
    }
}

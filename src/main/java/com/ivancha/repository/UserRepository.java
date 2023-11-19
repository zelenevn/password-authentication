package com.ivancha.repository;

import com.ivancha.entity.User;
import jakarta.persistence.EntityGraph;
import jakarta.persistence.EntityManager;

import java.util.Optional;


public class UserRepository extends RepositoryBase<Integer, User> {

    public UserRepository(EntityManager entityManager) {
        super(entityManager, User.class);
    }


    public Optional<User> findByNickname(String nickname) {
        var users = getEntityManager().createQuery("select u from User u where u.nickname = :nickname", User.class)
                .setParameter("nickname", nickname).getResultList();

        return users.size() == 0 ? Optional.empty() : Optional.of(users.get(0));
    }


    // TODO: 15.11.2023 Ничего, что он здесь каждый раз создаётся? Нам нужна сессия, чтобы его создать
    public EntityGraph<User> graphWithPassword() {

        var entityGraph = getEntityManager().createEntityGraph(User.class);
        entityGraph.addAttributeNodes("password");
        entityGraph.addSubgraph("password")
                .addAttributeNodes("timeBetweenPresses", "keyPressTime");
        
        return entityGraph;
    }
}

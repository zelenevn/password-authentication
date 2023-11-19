package com.ivancha.repository;

import com.ivancha.entity.Password;
import jakarta.persistence.EntityManager;


public class PasswordRepository extends RepositoryBase<Integer, Password> {

    public PasswordRepository(EntityManager entityManager) {
        super(entityManager, Password.class);
    }
}
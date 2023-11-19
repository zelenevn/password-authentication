package com.ivancha.repository;

import com.ivancha.entity.BaseEntity;

import java.io.Serializable;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Optional;


public interface Repository <K extends Serializable, E extends BaseEntity<K>> {

    E save(E entity);

    void delete(E entity);

    void update(E entity);

    default Optional<E> findById(K id)
    {
        return findById(id, Collections.emptyMap());
    }

    Optional<E> findById(K id, Map<String, Object> properties);

    default List<E> findAll()
    {
        return findAll(Collections.emptyMap());
    }

    List<E> findAll(Map<String, Object> hints);
}

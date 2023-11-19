package com.ivancha.repository;

import com.ivancha.entity.BaseEntity;
import jakarta.persistence.EntityManager;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

import java.io.Serializable;
import java.util.List;
import java.util.Map;
import java.util.Optional;


@RequiredArgsConstructor
public abstract class RepositoryBase<K extends Serializable, E extends BaseEntity<K>> implements Repository<K, E> {

    @Getter
    private final EntityManager entityManager;

    // можно попробовать убрать это поле, используя reflection
    private final Class<E> clazz;

    @Override
    public E save(E entity) {

        entityManager.persist(entity);

        return entity;
    }

    @Override
    public void delete(E entity)
    {
        entityManager.remove(entity);
        entityManager.flush();
    }

    @Override
    public void update(E entity) {

        entityManager.merge(entity);
    }

    @Override
    public Optional<E> findById(K id, Map<String, Object> properties) {

        return Optional.ofNullable(entityManager.find(clazz, id, properties));
    }

    @Override
    public List<E> findAll(Map<String, Object> hints) {

        var criteria = entityManager.getCriteriaBuilder().createQuery(clazz);
        criteria.from(clazz);

        var query = entityManager.createQuery(criteria);

        for (Map.Entry<String, Object> hint : hints.entrySet())
            query.setHint(hint.getKey(), hint.getValue());

        return query.getResultList();
    }
}

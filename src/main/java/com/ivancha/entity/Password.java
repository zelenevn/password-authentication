package com.ivancha.entity;

import jakarta.persistence.*;
import lombok.*;

import java.util.Map;


@EqualsAndHashCode(exclude = "user")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Entity
public class Password implements BaseEntity<Integer> {

    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    private Integer id;

    private String value;

    // по идее без optional = false запрос будет выполняться даже с LAZY, чтобы проверить есть ли значение
    @OneToOne(fetch = FetchType.LAZY)
    private User user;

    @ElementCollection()
    @CollectionTable(name = "time_between_presses")
    @MapKeyColumn(name = "gap_number")
    @Column(name = "time")
    private Map<Integer, Integer> timeBetweenPresses;

    @ElementCollection
    @CollectionTable(name = "key_press_time")
    @MapKeyColumn(name = "gap_number")
    @Column(name = "time")
    private Map<Integer, Integer> keyPressTime;
}

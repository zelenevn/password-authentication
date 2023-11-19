package com.ivancha.entity;

import jakarta.persistence.*;
import lombok.*;


@Builder
@ToString(exclude = "password")
@EqualsAndHashCode(of = "nickname")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "users")
public class User implements BaseEntity<Integer> {

    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    private Integer id;

    private String nickname;

    @OneToOne(mappedBy = "user", fetch = FetchType.LAZY)
    private Password password;
}


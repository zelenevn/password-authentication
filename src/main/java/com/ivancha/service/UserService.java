package com.ivancha.service;

import com.ivancha.dto.UserCreateDto;
import com.ivancha.dto.UserReadDto;
import com.ivancha.mapper.UserCreateMapper;
import com.ivancha.mapper.UserReadMapper;
import com.ivancha.repository.UserRepository;
import jakarta.transaction.Transactional;
import jakarta.validation.ConstraintViolationException;
import jakarta.validation.Validator;
import lombok.RequiredArgsConstructor;
import org.hibernate.graph.GraphSemantic;

import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;


@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final UserCreateMapper userCreateMapper;
    private final UserReadMapper userReadMapper;
    private final Validator validator;


    @Transactional
    public Integer create(UserCreateDto userDto) {

        var validationResult = validator.validate(userDto);
        if (!validationResult.isEmpty())
            throw new ConstraintViolationException(validationResult);

        var userEntity = userCreateMapper.map(userDto);
        return userRepository.save(userEntity).getId();
    }


    @Transactional
    public boolean delete(Integer id) {

        var mayBeUser = userRepository.findById(id);
        mayBeUser.ifPresent(userRepository::delete);

        return mayBeUser.isPresent();
    }

    @Transactional
    public Optional<UserReadDto> findByName(String nickname) {

        return userRepository.findByNickname(nickname)
                .map(userReadMapper::map);
    }

    @Transactional
    public List<UserReadDto> findAll() {

        // оптимизированный запрос сразу с password
        Map<String, Object> hints = Map.of(
                GraphSemantic.LOAD.getJakartaHintName(), userRepository.graphWithPassword()
        );
        return userRepository.findAll(hints).stream()
                .map(userReadMapper::map)
                .collect(Collectors.toList());
    }

}

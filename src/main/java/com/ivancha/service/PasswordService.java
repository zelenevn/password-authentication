package com.ivancha.service;

import com.ivancha.dto.PasswordCreateDto;
import com.ivancha.mapper.PasswordCreateMapper;
import com.ivancha.repository.PasswordRepository;
import jakarta.transaction.Transactional;
import jakarta.validation.ConstraintViolationException;
import jakarta.validation.Validator;
import lombok.RequiredArgsConstructor;


@RequiredArgsConstructor
public class PasswordService {


    private final PasswordRepository passwordRepository;
    private final PasswordCreateMapper passwordCreateMapper;
    private final Validator validator;


    @Transactional
    public Integer create(PasswordCreateDto passwordCreateDto) {

        var validationResult = validator.validate(passwordCreateDto);
        if (!validationResult.isEmpty())
            throw new ConstraintViolationException(validationResult);

        var passwordEntity = passwordCreateMapper.map(passwordCreateDto);
        return passwordRepository.save(passwordEntity).getId();
    }

}

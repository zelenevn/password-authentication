package com.ivancha.service;

import com.ivancha.dto.PasswordCreateDto;
import com.ivancha.entity.Password;
import com.ivancha.mapper.PasswordCreateMapper;
import com.ivancha.repository.PasswordRepository;
import com.ivancha.service.PasswordService;
import jakarta.validation.Validator;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Collections;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.doReturn;


@ExtendWith(MockitoExtension.class)
public class PasswordServiceTest {

    @Mock
    private PasswordRepository passwordRepository;

    @Mock
    private PasswordCreateMapper passwordCreateMapper;

    @Mock
    private Validator validator;

    @InjectMocks
    private PasswordService passwordService;


    @Test
    public void shouldReturnEntityId() {

        var passwordWithId = new Password(45346768, null, null, null, null);
        var password= new Password();
        var passwordCreateDto = new PasswordCreateDto(null, null, null, null);
        Integer id = 45346768;

        doReturn(passwordWithId)
                .when(passwordRepository).save(password);

        doReturn(Collections.emptySet())
                .when(validator).validate(passwordCreateDto);

        doReturn(password)
                .when(passwordCreateMapper).map(passwordCreateDto);

        var passwordId = passwordService.create(passwordCreateDto);
        assertThat(passwordId).isEqualTo(id);
    }
}

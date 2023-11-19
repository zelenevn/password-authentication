package com.ivancha.validation;

import com.ivancha.entity.User;
import com.ivancha.repository.UserRepository;
import com.ivancha.validation.impl.UserExistValidator;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.doReturn;


@ExtendWith(MockitoExtension.class)
public class UserExistValidatorTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserExistValidator userExistValidator;

    @Test
    public void shouldValidateObject() {

        Integer userId = 32;
        doReturn(Optional.of(new User()))
                .when(userRepository).findById(userId);

        var validResult = userExistValidator.isValid(userId, null);

        assertThat(validResult).isTrue();
    }

    @Test
    public void shouldNotBeValidated() {

        Integer userId = 32;
        doReturn(Optional.empty())
                .when(userRepository).findById(userId);

        var validResult = userExistValidator.isValid(userId, null);

        assertThat(validResult).isFalse();
    }
}

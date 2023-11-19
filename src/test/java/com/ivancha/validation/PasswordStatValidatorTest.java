package com.ivancha.validation;

import com.ivancha.dto.PasswordCreateDto;
import com.ivancha.validation.impl.PasswordStatValidator;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;

import java.util.Map;

import static org.assertj.core.api.Assertions.assertThat;


@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public class PasswordStatValidatorTest {

    private final PasswordStatValidator passwordStatValidator = new PasswordStatValidator();


    @Test
    public void shouldValidateObject() {

        var data = new PasswordCreateDto("hdsd", null,
                Map.of(1, 5, 2, 23, 3, 423),
                Map.of(1, 43, 2, 432, 3, 12, 4, 2));

        var validResult = passwordStatValidator.isValid(data, null);

        assertThat(validResult).isTrue();
    }

    @Test
    public void shouldNotBeValidated() {

        var data = new PasswordCreateDto("hdsd", null,
                Map.of(1, 5, 3, 423),
                Map.of(1, 43, 2, 432, 3, 12, 4, 2));

        var validResult = passwordStatValidator.isValid(data, null);

        assertThat(validResult).isFalse();
    }
}

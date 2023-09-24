package ru.phoekoby.bmil.backend.service;

import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import lombok.experimental.NonFinal;
import org.apache.commons.lang3.ArrayUtils;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import ru.phoekoby.bmil.backend.dto.GeneratePasswordDto;
import ru.phoekoby.bmil.backend.service.impl.PasswordServiceImpl;

import java.util.Arrays;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertTrue;

@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
@SpringBootTest
@RequiredArgsConstructor
public class PasswordServiceTest {

    @NonFinal
    @Autowired
    PasswordServiceImpl passwordService;

    Long length = 10L;
    Set<Character> alphabet = Set.of('a', 'b', 'c', 'd');
    GeneratePasswordDto dto = GeneratePasswordDto.builder()
            .alphabet(alphabet)
            .length(length)
            .build();

    @Test
    public void testGenerator() {
        String pass1 = passwordService.generatePassword(dto);
        String pass2 = passwordService.generatePassword(dto);
        System.out.printf(pass2);
        Assertions.assertEquals(pass1.length(), length);
        Assertions.assertEquals(pass2.length(), length);
        Assertions.assertNotEquals(pass2, pass1);

        Arrays.stream(ArrayUtils.toObject(pass2.toCharArray()))
                .forEach(character -> assertTrue(alphabet.contains(character)));
    }
}

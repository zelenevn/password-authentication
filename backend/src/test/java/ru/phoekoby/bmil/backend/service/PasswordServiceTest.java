package ru.phoekoby.bmil.backend.service;

import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import lombok.experimental.NonFinal;
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
        Character[] pass1 = passwordService.generatePassword(dto);
        Character[] pass2 = passwordService.generatePassword(dto);
        Assertions.assertEquals(pass1.length, length);
        Assertions.assertEquals(pass2.length, length);
        Assertions.assertNotEquals(pass2, pass1);

        Arrays.stream(pass2)
                .forEach(character -> assertTrue(alphabet.contains(character)));
    }
}

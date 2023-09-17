package ru.phoekoby.bmil.backend.service.impl;

import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.stereotype.Service;
import ru.phoekoby.bmil.backend.dto.GeneratePasswordDto;
import ru.phoekoby.bmil.backend.service.PasswordService;

import java.util.List;
import java.util.Random;

@Service
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class PasswordServiceImpl implements PasswordService {
    @Override
    public String generatePassword(GeneratePasswordDto dto) {
        List<Character> alphabet = dto.getAlphabet().stream().toList();
        return new Random()
                .ints(0, alphabet.size())
                .limit(dto.getLength())
                .mapToObj(alphabet::get)
                .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
                .toString();
    }
}

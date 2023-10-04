package ru.phoekoby.bmil.backend.service;

import ru.phoekoby.bmil.backend.dto.GeneratePasswordDto;

public interface PasswordService {
    Character[] generatePassword(GeneratePasswordDto dto);
}

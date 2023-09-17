package ru.phoekoby.bmil.backend.service;

import ru.phoekoby.bmil.backend.dto.GeneratePasswordDto;

public interface PasswordService {
    String generatePassword(GeneratePasswordDto dto);
}

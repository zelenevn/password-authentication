package ru.phoekoby.bmil.backend.controller;

import jakarta.validation.Valid;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ru.phoekoby.bmil.backend.dto.GeneratePasswordDto;
import ru.phoekoby.bmil.backend.service.PasswordService;

@RestController
@RequiredArgsConstructor
@FieldDefaults(makeFinal = true, level = AccessLevel.PRIVATE)
@RequestMapping("/api")
public class PasswordController {
    PasswordService passwordService;

    @PostMapping("/generate")
    public Character[] generatePassword(@Valid @RequestBody GeneratePasswordDto dto){
        return passwordService.generatePassword(dto);
    }
}

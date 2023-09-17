package ru.phoekoby.bmil.backend.dto;

import lombok.*;
import lombok.experimental.FieldDefaults;
import lombok.extern.jackson.Jacksonized;

import java.util.Set;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
@Jacksonized
public class GeneratePasswordDto {
    Long length;
    Set<Character> alphabet;
}

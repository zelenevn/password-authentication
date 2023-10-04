package ru.phoekoby.bmil.backend.dto;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.Size;
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
    @Min(8)
    Long length;
    @Size(min = 4)
    Set<Character> alphabet;
}

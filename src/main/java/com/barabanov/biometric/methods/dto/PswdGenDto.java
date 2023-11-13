package com.barabanov.biometric.methods.dto;

import com.barabanov.biometric.methods.password.generation.alphabet.Alphabet;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.NotNull;
import lombok.Getter;
import lombok.RequiredArgsConstructor;


import java.util.List;


@Getter
@RequiredArgsConstructor
public class PswdGenDto
{
    @Min(0)
    @NotNull
    private final Integer length;

    @NotEmpty
    private final List<Alphabet> alphabets;
}

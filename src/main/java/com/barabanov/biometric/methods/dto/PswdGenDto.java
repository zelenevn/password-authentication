package com.barabanov.biometric.methods.dto;

import com.barabanov.biometric.methods.password.generation.alphabet.Alphabet;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

import javax.validation.constraints.Min;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;
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

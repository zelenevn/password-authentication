package com.barabanov.biometric.methods.controller;

import com.barabanov.biometric.methods.password.generation.Alphabet;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;


@NoArgsConstructor
@Data
public class PasswordGenForm
{
    private List<Alphabet> alphabets;
    private int length;
}


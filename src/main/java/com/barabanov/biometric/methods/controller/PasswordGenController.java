package com.barabanov.biometric.methods.controller;

import com.barabanov.biometric.methods.password.generation.PasswordGenService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class PasswordGenController
{

    private final PasswordGenService passwordGenService;


    @Autowired
    public PasswordGenController(PasswordGenService passwordGenService) {
        this.passwordGenService = passwordGenService;
    }


    @GetMapping(value = "/generate")
    public ResponseEntity<String> generate(
            @RequestBody PasswordGenForm passwordGenForm)
    {
        String password = passwordGenService.generate(passwordGenForm.getAlphabets(), passwordGenForm.getLength());

        return new ResponseEntity<>(password, HttpStatus.OK);
    }

}

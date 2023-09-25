package com.barabanov.biometric.methods.controller;

import com.barabanov.biometric.methods.dto.PswdGenDto;
import com.barabanov.biometric.methods.mapper.PswdGenMapper;
import com.barabanov.biometric.methods.service.PasswordGenService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;


@RestController
public class PasswordGenController
{

    private final PasswordGenService passwordGenService;
    private final PswdGenMapper pswdGenMapper;


    @Autowired
    public PasswordGenController(PasswordGenService passwordGenService, PswdGenMapper pswdGenMapper) {
        this.passwordGenService = passwordGenService;
        this.pswdGenMapper = pswdGenMapper;
    }


    @GetMapping(value = "/generate")
    public ResponseEntity<?> generate(
            @RequestBody String pswdInfoAsJson)
    {
        @Valid
        PswdGenDto pswdGenDto = pswdGenMapper.mapFrom(pswdInfoAsJson);

        char[] password = passwordGenService.generate(pswdGenDto.getAlphabets(), pswdGenDto.getLength());

        return new ResponseEntity<>(password, HttpStatus.OK);
    }

}

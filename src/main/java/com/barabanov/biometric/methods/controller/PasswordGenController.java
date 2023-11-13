package com.barabanov.biometric.methods.controller;

import com.barabanov.biometric.methods.dto.PswdGenDto;
import com.barabanov.biometric.methods.mapper.PswdGenMapper;
import com.barabanov.biometric.methods.service.AlphabetService;
import com.barabanov.biometric.methods.service.PasswordGenService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
public class PasswordGenController
{

    private final PasswordGenService passwordGenService;
    private final AlphabetService alphabetService;
    private final PswdGenMapper pswdGenMapper;


    @Autowired
    public PasswordGenController(PasswordGenService passwordGenService, AlphabetService alphabetService, PswdGenMapper pswdGenMapper)
    {
        this.passwordGenService = passwordGenService;
        this.alphabetService = alphabetService;
        this.pswdGenMapper = pswdGenMapper;
    }


    @PostMapping(value = "/generate")
    public ResponseEntity<?> generate(
            @RequestBody String pswdInfoAsJson)
    {
        // TODO: 27.09.2023 Думаю, что мне не нужен маппер и можно встраиваться в механизм маппинга json -> entity самого спринга
        // TODO: 27.09.2023 не работает валидация
        @Valid
        PswdGenDto pswdGenDto = pswdGenMapper.mapFrom(pswdInfoAsJson);

        char[] password = passwordGenService.generate(pswdGenDto.getAlphabets(), pswdGenDto.getLength());

        return new ResponseEntity<>(password, HttpStatus.OK);
    }


    @GetMapping(value = "/groups")
    public ResponseEntity<?> groups()
    {
        return new ResponseEntity<>(alphabetService.getGroups(), HttpStatus.OK);
    }


    @GetMapping(value = "/group")
    public ResponseEntity<?> alphabetsInGroup(@RequestParam(value = "g") String groupName)
    {
        return new ResponseEntity<>(alphabetService.getAlphabetSimpleNames(groupName), HttpStatus.OK);
    }

}

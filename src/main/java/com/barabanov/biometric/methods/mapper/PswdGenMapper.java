package com.barabanov.biometric.methods.mapper;

import com.barabanov.biometric.methods.dto.PswdGenDto;
import com.barabanov.biometric.methods.service.AlphabetService;
import com.google.gson.Gson;
import org.springframework.stereotype.Component;


@Component("pswdGenMapper")
public class PswdGenMapper implements Mapper<String, PswdGenDto>
{
    private final Gson gson;

    public PswdGenMapper(AlphabetService alphabetService, Gson gson)
    {
        this.gson = gson;
    }


    @Override
    public PswdGenDto mapFrom(String pswdInfoAsJson)
    {
        return gson.fromJson(pswdInfoAsJson, PswdGenDto.class);
    }
}

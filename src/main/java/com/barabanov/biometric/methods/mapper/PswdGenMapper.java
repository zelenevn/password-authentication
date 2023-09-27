package com.barabanov.biometric.methods.mapper;

import com.barabanov.biometric.methods.dto.PswdGenDto;
import com.barabanov.biometric.methods.json.serializer.PswdGenDtoDeserializer;
import com.barabanov.biometric.methods.service.AlphabetService;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;


@Component("pswdGenMapper")
public class PswdGenMapper implements Mapper<String, PswdGenDto>
{
    private final Gson gson;

    @Autowired
    public PswdGenMapper(AlphabetService alphabetService)
    {
        // TODO: 27.09.2023 для этого нужен DI
        this.gson = new GsonBuilder()
                .registerTypeAdapter(PswdGenDto.class,  new PswdGenDtoDeserializer(alphabetService))
                .create();
    }


    @Override
    public PswdGenDto mapFrom(String pswdInfoAsJson)
    {
        return gson.fromJson(pswdInfoAsJson, PswdGenDto.class);
    }
}

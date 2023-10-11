package com.barabanov.biometric.methods;

import com.barabanov.biometric.methods.dto.PswdGenDto;
import com.barabanov.biometric.methods.json.serializer.PswdGenDtoDeserializer;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;


@SpringBootApplication
public class RestApplication
{
    public static void main(String[] args)
    {
         SpringApplication.run(RestApplication.class, args);
    }

    @Bean
    public Gson gson(PswdGenDtoDeserializer pswdGenDtoDeserializer)
    {
        return new GsonBuilder()
                .registerTypeAdapter(PswdGenDto.class, pswdGenDtoDeserializer)
                .create();
    }

}
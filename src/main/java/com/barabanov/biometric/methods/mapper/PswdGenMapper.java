package com.barabanov.biometric.methods.mapper;

import com.barabanov.biometric.methods.dto.PswdGenDto;
import com.barabanov.biometric.methods.service.AlphabetService;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;


@Component("pswdGenMapper")
public class PswdGenMapper implements Mapper<String, PswdGenDto>
{
    private final AlphabetService alphabetService;


    @Autowired
    public PswdGenMapper(AlphabetService alphabetService) {
        this.alphabetService = alphabetService;
    }


    @Override
    public PswdGenDto mapFrom(String pswdInfoAsJson)
    {
        try {
            JSONObject jo = (JSONObject) new JSONParser().parse(pswdInfoAsJson);

            Object objLength = jo.get("length");
            Integer length = objLength != null ? ((Long) objLength).intValue(): null;

            List<String> alphabetNames = new ArrayList<>();
            Object objAlphabet = jo.get("alphabets");
            if (objAlphabet != null)
                for (Object object : (JSONArray) objAlphabet)
                    alphabetNames.add((String) object);

            return new PswdGenDto(length, alphabetService.determineAlphabets(alphabetNames));
        } catch (ParseException e) {
            // TODO: 25.09.2023 somehow handle the error
            throw new RuntimeException(e);
        }
    }
}

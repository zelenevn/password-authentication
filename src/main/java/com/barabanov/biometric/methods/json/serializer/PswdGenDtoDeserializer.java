package com.barabanov.biometric.methods.json.serializer;

import com.barabanov.biometric.methods.dto.PswdGenDto;
import com.barabanov.biometric.methods.service.AlphabetService;
import com.google.gson.*;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


@Component
@RequiredArgsConstructor
public class PswdGenDtoDeserializer implements JsonDeserializer<PswdGenDto>
{

    private final AlphabetService alphabetService;


    // Если указать ону и ту же группу дважды, то значения не добавятся, а перезапишутся
    @Override
    public PswdGenDto deserialize(JsonElement json, Type typeOfT, JsonDeserializationContext context)
            throws JsonParseException
    {
        JsonObject jsonObject = json.getAsJsonObject();
        int length = jsonObject.get("length").getAsInt();
        JsonArray groups = jsonObject.getAsJsonArray("groups");

        Map<String, List<String>> groupToAlphabets = new HashMap<>();
        for (JsonElement groupAsElem : groups)
        {
            JsonObject groupAsJObg =  (JsonObject) groupAsElem;
            String alphabetGroup = groupAsJObg.get("group").getAsString();

            List<String> alphabets = new ArrayList<>();
            JsonArray alphabetsInGroup = groupAsJObg.getAsJsonArray("alphabets");
            for (JsonElement alphabetAsElem : alphabetsInGroup)
                alphabets.add(alphabetAsElem.getAsString());

            groupToAlphabets.put(alphabetGroup, alphabets);
        }

        return new PswdGenDto(length, alphabetService.determineAlphabets(groupToAlphabets));
    }
}


package ru.phoekoby.bmil.backend.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.AccessLevel;
import lombok.experimental.FieldDefaults;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
import ru.phoekoby.bmil.backend.dto.GeneratePasswordDto;
import ru.phoekoby.bmil.backend.service.PasswordService;

import java.util.Set;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@FieldDefaults(level = AccessLevel.PRIVATE)
@RunWith(SpringRunner.class)
@WebMvcTest(PasswordController.class)
public class PasswordControllerTest {
    @Autowired
    MockMvc mockMvc;

    @Autowired
    ObjectMapper objectMapper;

    @MockBean
    PasswordService passwordService;
    @Test
    public void testGeneratePassword() throws Exception {
        GeneratePasswordDto dto = GeneratePasswordDto.builder()
                .alphabet(Set.of('a', 'b', 'c', 'd', 'e'))
                .length(8L)
                .build();

        mockMvc.perform(post("/api/generate")
                        .content(objectMapper.writeValueAsBytes(dto))
                        .contentType("application/json")
                        .accept(MediaType.parseMediaType("application/json")))
                .andExpect(status().isOk());

    }

    @Test
    public void testGeneratePasswordWithNotValidLength() throws Exception {
        GeneratePasswordDto dto = GeneratePasswordDto.builder()
                .alphabet(Set.of('a', 'b', 'c', 'd', 'e'))
                .length(7L)
                .build();
        mockMvc.perform(post("/api/generate")
                        .content(objectMapper.writeValueAsBytes(dto))
                        .contentType("application/json")
                        .accept(MediaType.parseMediaType("application/json")))
                .andExpect(status().isBadRequest());

    }

    @Test
    public void testGeneratePasswordWithNotValidAlphabet() throws Exception {
        GeneratePasswordDto dto = GeneratePasswordDto.builder()
                .alphabet(Set.of('a', 'b', 'c'))
                .length(8L)
                .build();
        mockMvc.perform(post("/api/generate")
                        .content(objectMapper.writeValueAsBytes(dto))
                        .contentType("application/json")
                        .accept(MediaType.parseMediaType("application/json")))
                .andExpect(status().isBadRequest());

    }
}

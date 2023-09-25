package service;

import com.barabanov.biometric.methods.password.generation.alphabet.Alphabet;
import com.barabanov.biometric.methods.service.AlphabetService;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import static org.assertj.core.api.Assertions.assertThat;


public class AlphabetServiceTest
{

    private final AlphabetService alphabetService = new AlphabetService();

    @Test
    public void shouldDetermineOrdinaryAlphabet()
    {
        List<String> alphabetNames = Arrays.asList("LATIN_LOWERCASE", "LATIN_UPPERCASE","CYRILLIC_UPPERCASE",
                "CYRILLIC_LOWERCASE", "SPACE", "SPECIAL_SYM", "NUMBERS");

        List<Alphabet> alphabets = alphabetService.determineAlphabets(alphabetNames);

        assertThat(
                alphabets.stream().map(Object::toString).collect(Collectors.toList()))
                .containsExactlyInAnyOrderElementsOf(alphabetNames);

    }
}

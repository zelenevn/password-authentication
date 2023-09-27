package service;

import com.barabanov.biometric.methods.password.generation.alphabet.Alphabet;
import com.barabanov.biometric.methods.password.generation.alphabet.Latin;
import com.barabanov.biometric.methods.service.AlphabetService;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;

import java.util.*;
import java.util.stream.Collectors;

import static org.assertj.core.api.Assertions.assertThat;


@TestInstance(value = TestInstance.Lifecycle.PER_CLASS)
public class AlphabetServiceTest
{

    private final AlphabetService alphabetService = new AlphabetService();


    @Test
    public void shouldDetermineOrdinaryAlphabets()
    {
        Map<String, List<String>> alphabets = new HashMap<>();
        alphabets.put("Cyrillic", Arrays.asList("LOWERCASE", "UPPERCASE"));
        alphabets.put("Latin", Arrays.asList("LOWERCASE", "UPPERCASE"));
        alphabets.put("Symbol", Arrays.asList("NUMBERS", "SPACE", "SPECIAL"));

        List<Alphabet> determineAlphabets = alphabetService.determineAlphabets(alphabets);

        List<String> alphabetSimpleNames = alphabets.values().stream()
                .flatMap(Collection::stream)
                .collect(Collectors.toList());
        assertThat(
                determineAlphabets.stream().map(Object::toString).collect(Collectors.toList()))
                .containsExactlyInAnyOrderElementsOf(alphabetSimpleNames);
    }


    @Test
    public void shouldGiveAlphabetSimpleNamesForLatin()
    {

        List<String> latinAlphabetNames = new ArrayList<>();
        Class<? extends Alphabet> latinGroup = Latin.class;

        for (Alphabet alphabet : latinGroup.getEnumConstants())
            latinAlphabetNames.add(alphabet.toString().toLowerCase());

        @SuppressWarnings("all") // because I didn't find another suitable one. "null" - does't work
        List<String> determinedNames = alphabetService.getAlphabetSimpleNames("Latin");

        assertThat(determinedNames).containsExactlyInAnyOrderElementsOf(latinAlphabetNames);
    }

}

package password.generation;

import com.barabanov.biometric.methods.password.generation.Alphabet;
import com.barabanov.biometric.methods.password.generation.PasswordGenService;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import static com.barabanov.biometric.methods.password.generation.Alphabet.*;
import static org.assertj.core.api.Assertions.assertThat;


public class PasswordGenServiceTest
{

    private static final PasswordGenService passwordGenService = new PasswordGenService();


    @Test
    public void shouldGeneratePswdFromOrdinaryAlphabet()
    {
        List<Alphabet> alphabets = Arrays.asList(LATIN_LOWERCASE, LATIN_UPPERCASE, NUMBERS,
                SPECIAL_SYM, SPACE, CYRILLIC_LOWERCASE, CYRILLIC_UPPERCASE);
        char[] password = passwordGenService.generate(alphabets, 20);

        Set<Character> alphabet = alphabets.stream()
                .flatMap(alphabetName -> alphabetName.getSymbols().stream())
                .collect(Collectors.toSet());

        assertThat(password).hasSize(20);
        for (char sym : password)
            assertThat(sym).isIn(alphabet);
    }


    @Test
    public void shouldReplaceElementsWith0()
    {
        char[] password = new char[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        passwordGenService.erasePswd(password);

        assertThat(password).containsOnly((char) 0);
    }

}

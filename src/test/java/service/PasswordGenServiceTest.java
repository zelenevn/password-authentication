package service;

import com.barabanov.biometric.methods.password.generation.alphabet.Alphabet;
import com.barabanov.biometric.methods.password.generation.alphabet.Cyrillic;
import com.barabanov.biometric.methods.password.generation.alphabet.Latin;
import com.barabanov.biometric.methods.password.generation.alphabet.Symbol;
import com.barabanov.biometric.methods.service.PasswordGenService;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import static com.barabanov.biometric.methods.password.generation.alphabet.Symbol.NUMBERS;
import static org.assertj.core.api.Assertions.assertThat;


@TestInstance(value = TestInstance.Lifecycle.PER_CLASS)
public class PasswordGenServiceTest
{

    private static final PasswordGenService passwordGenService = new PasswordGenService();


    @Test
    public void shouldUseNewEnum()
    {
        char[] password = passwordGenService.generate(Collections.singletonList(NewEnum.E), 20);

        assertThat(password).hasSize(20);
        for (char sym : password)
            assert(NewEnum.E.getSymbols().contains(sym));

    }


    @Test
    public void shouldUse2Enums()
    {

        List<Alphabet> alphabets = Arrays.asList(NUMBERS, NewEnum.E);
        char[] password = passwordGenService.generate(alphabets, 20);

        Set<Character> alphabet = alphabets.stream()
                .flatMap(alphabetName -> alphabetName.getSymbols().stream())
                .collect(Collectors.toSet());

        assertThat(password).hasSize(20);
        for (char sym : password)
            assertThat(sym).isIn(alphabet);
    }



    private enum NewEnum implements Alphabet
    {
        E (Arrays.asList('a', '$', 'c'));

        private final List<Character> symbols;

        NewEnum(List<Character> symbols)
        {
            this.symbols = symbols;
        }

        @Override
        public List<Character> getSymbols() {
            return symbols;
        }
    }


    @Test
    public void shouldGeneratePswdWithOrdinaryAlphabets()
    {
        List<Alphabet> alphabets = Arrays.asList(
                Latin.LOWERCASE, Latin.UPPERCASE,
                Cyrillic.LOWERCASE, Cyrillic.UPPERCASE,
                Symbol.NUMBERS, Symbol.SPECIAL, Symbol.SPACE
                );

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

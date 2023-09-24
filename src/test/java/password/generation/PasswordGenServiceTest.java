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
    private final PasswordGenService passwordGenService = new PasswordGenService();

    /*
    @Test
    public void shouldUseNewEnum()
    {
        enum NewEnum implements Alphabet
        {
            E (Set.of('a', 'b', 'c', '1'));

            private final Set<Character> symbols;

            NewEnum(Set<Character> symbols)
            {
                this.symbols = symbols;
            }

            @Override
            public Set<Character> getSymbols() {
                return symbols;
            }
        }

        String password = passwordGenService.generate(Set.of(NewEnum.E), 20);

        assertThat(password).hasSize(20);
        for (char sym : password.toCharArray())
            assert(NewEnum.E.getSymbols().contains(sym));

    }
     */


    @Test
    public void shouldGeneratePswdFromOrdinaryAlphabet()
    {
        List<Alphabet> alphabets = Arrays.asList(LATIN_LOWERCASE, LATIN_UPPERCASE, NUMBERS,
                SPECIAL_SYM, SPACE, CYRILLIC_LOWERCASE, CYRILLIC_UPPERCASE);
        String password = passwordGenService.generate(alphabets, 20);

        Set<Character> alphabet = alphabets.stream()
                .flatMap(alphabetName -> alphabetName.getSymbols().stream())
                .collect(Collectors.toSet());

        assertThat(password).hasSize(20);
        for (char sym : password.toCharArray())
            assertThat(sym).isIn(alphabet);
    }


}

package mapper;

import com.barabanov.biometric.methods.dto.PswdGenDto;
import com.barabanov.biometric.methods.mapper.PswdGenMapper;
import com.barabanov.biometric.methods.service.AlphabetService;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static com.barabanov.biometric.methods.password.generation.alphabet.OrdinaryAlphabet.*;
import static org.assertj.core.api.Assertions.assertThat;


public class MapperTest
{

    private static final PswdGenMapper pswdGenMapper = new PswdGenMapper(new AlphabetService());

    @Test
    public void testMapping()
    {
        String pswdInfoAsJson = "{\n" +
                "    \"alphabets\" : [\"LATIN_LOWERCASE\", \"NUMBERS\", \"SPECIAL_SYM\"],\n" +
                "    \"length\" : 8\n" +
                "}";

        PswdGenDto pswdGenDto = pswdGenMapper.mapFrom(pswdInfoAsJson);

        assertThat(pswdGenDto.getLength()).isEqualTo(8);
        assertThat(pswdGenDto.getAlphabets()).containsExactlyInAnyOrderElementsOf(
                Arrays.asList(LATIN_LOWERCASE, NUMBERS, SPECIAL_SYM)
        );
    }
}

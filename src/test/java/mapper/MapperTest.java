package mapper;

import com.barabanov.biometric.methods.dto.PswdGenDto;
import com.barabanov.biometric.methods.json.serializer.PswdGenDtoDeserializer;
import com.barabanov.biometric.methods.mapper.PswdGenMapper;
import com.barabanov.biometric.methods.password.generation.alphabet.Cyrillic;
import com.barabanov.biometric.methods.password.generation.alphabet.Latin;
import com.barabanov.biometric.methods.password.generation.alphabet.Symbol;
import com.barabanov.biometric.methods.service.AlphabetService;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;

import java.util.Arrays;

import static org.assertj.core.api.Assertions.assertThat;


@TestInstance(value = TestInstance.Lifecycle.PER_CLASS)
public class MapperTest
{
    private static final Gson gson = new GsonBuilder()
            .registerTypeAdapter(PswdGenDto.class, new PswdGenDtoDeserializer(new AlphabetService()))
            .create();

    private static final PswdGenMapper pswdGenMapper = new PswdGenMapper(new AlphabetService(), gson);


    @Test
    public void testMapping()
    {
        String pswdInfoAsJson = "{\n" +
                "    \"length\" : 34,\n" +
                "    \"groups\" : [\n" +
                "        {\n" +
                "            \"group\" : \"latin\",\n" +
                "            \"alphabets\" : [\"lowercase\", \"uppercase\"]\n" +
                "        },\n" +
                "        {\n" +
                "            \"group\" : \"Symbol\",\n" +
                "            \"alphabets\" : [\"special\", \"numbers\", \"space\"]\n" +
                "        },\n" +
                "        {\n" +
                "            \"group\" : \"cyrillic\",\n" +
                "            \"alphabets\" : [\"lowercase\", \"uppercase\"]\n" +
                "        }\n" +
                "    ]\n" +
                "}";

        PswdGenDto pswdGenDto = pswdGenMapper.mapFrom(pswdInfoAsJson);

        assertThat(pswdGenDto.getLength()).isEqualTo(34);
        assertThat(pswdGenDto.getAlphabets()).containsExactlyInAnyOrderElementsOf(
                Arrays.asList(Cyrillic.LOWERCASE, Cyrillic.UPPERCASE,
                        Latin.LOWERCASE, Latin.UPPERCASE,
                        Symbol.NUMBERS, Symbol.SPACE, Symbol.SPECIAL)
        );
    }
}

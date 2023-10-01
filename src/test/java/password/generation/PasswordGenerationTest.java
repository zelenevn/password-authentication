package password.generation;

import com.emelyanova.password.generation.PasswordGenerator;
import org.junit.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

public class PasswordGenerationTest {

    @Test
    public void passwordGenerationTest() {
        List<Character> alphabet = List.of('s', 'd', '1', '@', '&', 'g');
        int pswdLen = 35;
        String password = PasswordGenerator.password(pswdLen, alphabet);

        assertThat(password).hasSize(pswdLen);

        for (char ch : password.toCharArray())
            assertThat(ch).isIn(alphabet);
    }
}

package password.generation;

import com.ivancha.biometry.alphabet.EmptyAbc;
import com.ivancha.biometry.alphabet.EnglishLowercaseAbc;
import com.ivancha.biometry.alphabet.NumberAbc;
import com.ivancha.biometry.password.PasswordUtil;
import org.junit.Test;

import static org.assertj.core.api.Assertions.assertThat;


public class PasswordUtilTest {


    @Test
    public void passwordGenerationTest(){

        var emptyAbc = new EmptyAbc();
        var englishLowercaseAbc = new EnglishLowercaseAbc(emptyAbc);
        var numberAbc = new NumberAbc(englishLowercaseAbc);
        int passwordSize = 34;

        var password = PasswordUtil.generate(numberAbc, passwordSize);

        assertThat(password).hasSize(passwordSize);

        for (char ch : password.toCharArray())
            assertThat(ch).isIn(numberAbc.getLetters());

    }
}

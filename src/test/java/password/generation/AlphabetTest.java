package password.generation;

import com.ivancha.biometry.alphabet.*;
import org.junit.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;


public class AlphabetTest {


    @Test
    public void AlphabetCreationTest() throws NoSuchFieldException, IllegalAccessException {

        var emptyAbc = new EmptyAbc();
        var cyrillicLowercaseAbc = new CyrillicLowercaseAbc(emptyAbc);
        var cyrillicUppercaseAbc = new CyrillicUppercaseAbc(cyrillicLowercaseAbc);
        var englishLowercaseAbc = new EnglishLowercaseAbc(cyrillicUppercaseAbc);
        var englishUppercaseAbc = new EnglishUppercaseAbc(englishLowercaseAbc);
        var numberAbc = new NumberAbc(englishUppercaseAbc);
        var specialSymAbc = new SpecialSymAbc(numberAbc);

        List<Character> mergedAlphabet = specialSymAbc.getLetters();

        assertThat(mergedAlphabet).containsAll(getLetters(CyrillicLowercaseAbc.class, cyrillicLowercaseAbc));
        assertThat(mergedAlphabet).containsAll(getLetters(CyrillicUppercaseAbc.class, cyrillicUppercaseAbc));
        assertThat(mergedAlphabet).containsAll(getLetters(EnglishLowercaseAbc.class, englishLowercaseAbc));
        assertThat(mergedAlphabet).containsAll(getLetters(EnglishUppercaseAbc.class, englishUppercaseAbc));
        assertThat(mergedAlphabet).containsAll(getLetters(NumberAbc.class, numberAbc));
        assertThat(mergedAlphabet).containsAll(getLetters(SpecialSymAbc.class, specialSymAbc));
        assertThat(mergedAlphabet).hasSize(33 * 2 + 26 * 2 + 10 + 20);
    }


    @SuppressWarnings("unchecked")
    private List<Character> getLetters(Class<?> clazz, Object obj) throws NoSuchFieldException, IllegalAccessException {

        var lettersField = clazz.getDeclaredField("letters");
        lettersField.setAccessible(true);

        return (List<Character>)lettersField.get(obj);
    }
}

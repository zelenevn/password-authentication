package ui;

import com.ivancha.biometry.alphabet.EmptyAbc;
import com.ivancha.biometry.alphabet.EnglishLowercaseAbc;
import com.ivancha.biometry.alphabet.NumberAbc;
import com.ivancha.biometry.ui.UiUtil;
import org.junit.Test;

import java.lang.reflect.InvocationTargetException;
import java.util.Collections;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;


public class UtilTest {

    @Test
    public void createAlphabetByAliasesTest() throws InvocationTargetException, NoSuchMethodException, InstantiationException, IllegalAccessException {

        var alphabet = UiUtil.createAlphabetByAliases(List.of(1, 3));

        var emptyAbc = new EmptyAbc();
        var englishLowercaseAbc = new EnglishLowercaseAbc(emptyAbc);
        var numberAbc = new NumberAbc(englishLowercaseAbc);

        assertThat(alphabet.getLetters()).containsExactlyInAnyOrderElementsOf(numberAbc.getLetters());
    }


    @Test
    public void createEmptyAlphabetByAliases() throws InvocationTargetException, NoSuchMethodException, InstantiationException, IllegalAccessException {

        var alphabet = UiUtil.createAlphabetByAliases(Collections.emptyList());

        assertThat(alphabet).isNotNull();
        assertThat(alphabet.getLetters()).hasSize(0);
    }
}

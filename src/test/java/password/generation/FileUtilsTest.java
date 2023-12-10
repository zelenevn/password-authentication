package password.generation;

import com.emelyanova.password.registration.FileUtils;
import org.junit.Test;

import java.util.Arrays;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

public class FileUtilsTest {

    @Test
    public void fileNamesTest() {
        String combOfAliases = "2,1,4,3";

        List<String> fileNames = FileUtils.fileNames(combOfAliases);

        assertThat(fileNames).containsExactlyInAnyOrderElementsOf(Arrays.asList("lower_case.txt",
                "upper_case.txt",
                "numbers.txt",
                "special_symbols.txt"));

    }

    @Test
    public void emptyFileNamesTest() {
        String combOfAliases = "5, 8, 12, 65";

        List<String> fileNames = FileUtils.fileNames(combOfAliases);

        assertThat(fileNames).isEmpty();
    }

    @Test
    public void readAlphabetTest() {
        var alphabet = FileUtils.readAlphabet("lower_case.txt");
        assertThat(alphabet).containsExactlyInAnyOrderElementsOf(List.of('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'));
    }
}

package password.generation;

import com.barabanov.biometric.methods.password.generation.Appraiser;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.AssertionsForClassTypes.within;

public class AppraiserTest {

    @Test
    public void quantificationOfDurabilityTest()
    {
        long time = 24 * 60 * 60 * 1000; // 1 day
        int speed = 1000 * 6; // 6 second per 1 password
        int passwordLen = 8;
        int alphabetSize = 26;

        assertThat(Appraiser.quantificationOfDurability(alphabetSize, passwordLen, time, speed))
                .isCloseTo(3.0 / 6_400_000, within(0.0001));
    }
}

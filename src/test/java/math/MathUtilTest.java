package math;

import com.ivancha.biometry.math.MathUtil;
import org.junit.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.AssertionsForClassTypes.within;

public class MathUtilTest {

    @Test
    public void dispersionTest() {
        List<Long> values = List.of(2L, 5L, 32L, 6L, 21L, 17L);
        double dispersion = MathUtil.dispersion(values);

        assertThat(dispersion).isCloseTo(111.806, within(0.001));
    }

    @Test
    public void mathExpectedValTest() {
        List<Long> values = List.of(2L, 5L, 32L, 6L, 21L, 17L);
        double avg = MathUtil.mathExpectedVal(values);

        assertThat(avg).isCloseTo(13.833, within(0.001));
    }
}

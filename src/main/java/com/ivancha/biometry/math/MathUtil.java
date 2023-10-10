package com.ivancha.biometry.math;

import java.util.List;

public class MathUtil {

    public static double dispersion(List<Long> numbers) {

        double avg = numbers.stream().reduce(0L, Long::sum) * 1.0 / numbers.size();

        return numbers.stream()
                .map(a -> a - avg)
                .map(a -> a * a)
                .reduce(0.0, Double::sum) / numbers.size();
    }

    public static double mathExpectedVal(List<Long> numbers) {
        return numbers.stream().reduce(0L, Long::sum) * 1.0 / numbers.size();
    }
}

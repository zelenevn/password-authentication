package domain;

import org.junit.jupiter.api.Test;
import org.testng.Assert;

import static org.junit.jupiter.api.Assertions.*;

class PasswordGeneratorTest {
    PasswordBuilder passwordBuilder = new PasswordGenerator();

    @Test
    void length() {
        Assert.assertEquals(10, passwordBuilder.generatePassword(10, false, false,
                false).length());
    }

    @Test
    void repeatingCharacters(){
        String password = passwordBuilder.generatePassword(10, false, false, false);

        for (int i = 1; i < password.length() - 1; i++) {
            String symbol = String.valueOf(password.charAt(i));
            String[] passwordSplit = password.split(symbol);
            assertFalse(passwordSplit[0].contains(symbol));
            assertFalse(passwordSplit[1].contains(symbol));
        }
    }
}
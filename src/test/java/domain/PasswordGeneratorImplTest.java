package domain;

import domain.generators.PasswordGenerator;
import domain.generators.PasswordGeneratorImpl;
import org.junit.jupiter.api.Test;
import org.testng.Assert;

import static org.junit.jupiter.api.Assertions.*;

class PasswordGeneratorImplTest {
    PasswordGenerator passwordGenerator = new PasswordGeneratorImpl();

    @Test
    void length() {
        Assert.assertEquals(10, passwordGenerator.generatePassword(10, false, false,
                false).length());
    }

    @Test
    void repeatingCharacters(){
        String password = passwordGenerator.generatePassword(10, false, false, false);

        for (int i = 1; i < password.length() - 1; i++) {
            String symbol = String.valueOf(password.charAt(i));
            String[] passwordSplit = password.split(symbol);
            assertFalse(passwordSplit[0].contains(symbol));
            assertFalse(passwordSplit[1].contains(symbol));
        }
    }
}
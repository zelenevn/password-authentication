package groupId.generators;

import groupId.EnglishAlphabet;
import org.junit.jupiter.api.Test;
import org.testng.Assert;

import java.security.SecureRandom;

import static org.testng.AssertJUnit.assertFalse;

class PasswordGeneratorImplTest {

    PasswordGenerator passwordGenerator = new PasswordGeneratorImpl(new SecureRandom());        // Arrange

    @Test
    void length() {
        // Ask
        int lengthPassword = passwordGenerator.generatePassword(10, new EnglishAlphabet()).length();

        // Assert
        Assert.assertEquals(10, lengthPassword);
    }

    @Test
    void repeatingCharacters() {
        // Ask
        String password = passwordGenerator.generatePassword(10, new EnglishAlphabet());

        // Assert
        for (int i = 1; i < password.length() - 1; i++) {
            String symbol = String.valueOf(password.charAt(i));
            String[] passwordSplit = password.split(symbol);
            assertFalse(passwordSplit[0].contains(symbol));
            assertFalse(passwordSplit[1].contains(symbol));
        }
    }

    @Test
    void presenceNumbers() {
        // Ask
        String passwordContainNumbers = "aaaaa1aa";
        String passwordNotContainNumbers = "aaaaaaaa";

        // Assert
        Assert.assertTrue(passwordGenerator.containNumbers(passwordContainNumbers));
        Assert.assertFalse(passwordGenerator.containNumbers(passwordNotContainNumbers));
    }

    @Test
    void presenceUpperCase() {
        // Ask
        String passwordContainUpperCase = "aaaaaAaa";
        String passwordNotContainUpperCase = "aaaaaaaa";

        // Assert
        Assert.assertTrue(passwordGenerator.containUpperCase(passwordContainUpperCase));
        Assert.assertFalse(passwordGenerator.containNumbers(passwordNotContainUpperCase));
    }

    @Test
    void presencePunctuationMarks() {
        // Ask
        String passwordContainMarks = "aaaaa,aa";
        String passwordNotContainMarks = "aaaaaaaa";

        // Assert
        Assert.assertTrue(passwordGenerator.containPunctuationMarks(passwordContainMarks));
        Assert.assertFalse(passwordGenerator.containPunctuationMarks(passwordNotContainMarks));
    }
}
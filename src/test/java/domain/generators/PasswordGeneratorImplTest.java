//package domain.generators;
//
//
//import domain.models.Alphabet;
//import org.junit.jupiter.api.Test;
//
//import org.testng.Assert;
//
//import static org.junit.jupiter.api.Assertions.assertFalse;
//
//class PasswordGeneratorImplTest {
//    PasswordGenerator passwordGenerator = new PasswordGeneratorImpl();
//
//    @Test
//    void length() {
//        int lengthPassword = passwordGenerator.generatePassword(10, new Alphabet()).length();
//        Assert.assertEquals(10, lengthPassword);
//    }
//
//    @Test
//    void repeatingCharacters() {
//        String password = passwordGenerator.generatePassword(10, new Alphabet());
//
//        for (int i = 1; i < password.length() - 1; i++) {
//            String symbol = String.valueOf(password.charAt(i));
//            String[] passwordSplit = password.split(symbol);
//            assertFalse(passwordSplit[0].contains(symbol));
//            assertFalse(passwordSplit[1].contains(symbol));
//        }
//    }
//
//    @Test
//    void presenceNumbers() {
//        String passwordContainNumbers = "aaaaa1aa";
//        String passwordNotContainNumbers = "aaaaaaaa";
//
//        Assert.assertTrue(passwordGenerator.containNumbers(passwordContainNumbers));
//        Assert.assertFalse(passwordGenerator.containNumbers(passwordNotContainNumbers));
//    }
//
//    @Test
//    void presenceUpperCase() {
//        String passwordContainUpperCase = "aaaaaAaa";
//        String passwordNotContainUpperCase = "aaaaaaaa";
//
//        Assert.assertTrue(passwordGenerator.containUpperCase(passwordContainUpperCase));
//        Assert.assertFalse(passwordGenerator.containNumbers(passwordNotContainUpperCase));
//    }
//
//    @Test
//    void presencePunctuationMarks() {
//        String passwordContainMarks = "aaaaa,aa";
//        String passwordNotContainMarks = "aaaaaaaa";
//
//        Assert.assertTrue(passwordGenerator.containPunctuationMarks(passwordContainMarks));
//        Assert.assertFalse(passwordGenerator.containPunctuationMarks(passwordNotContainMarks));
//    }
//}
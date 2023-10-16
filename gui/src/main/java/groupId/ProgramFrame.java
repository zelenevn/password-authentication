package groupId;

import groupId.generators.PasswordGenerator;
import groupId.generators.PasswordGeneratorImpl;
import groupId.listeners.ListenerKeyHold;
import groupId.listeners.ListenerKeyOverlayFirstType;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyListener;
import java.security.SecureRandom;

/**
 * Класс приложения
 *
 * @autor Pycukvsu
 */
public class ProgramFrame extends JFrame {
    private JPanel mainPanel;
    private JPanel panel2;
    private JButton button;
    private JTextField tfPhrase;
    private JTextArea taPassword1;
    private JTextArea taKeyHold;
    private JCheckBox cbUpperCase;
    private JCheckBox cbPunctuationMarks;
    private JCheckBox cbNumbers;
    private JTextField thPasswordLength;
    private JButton jButton2;
    private JComboBox<String> cbLanguage;
    private final PasswordGenerator passwordGenerator;
    private Alphabet alphabet = new EnglishAlphabet();

    public void showKeyHold(String averageKeyHold) {
        taKeyHold.setText(averageKeyHold);
    }

    public ProgramFrame() {
        passwordGenerator = new PasswordGeneratorImpl(new SecureRandom());
        cbLanguage.addItem("English");
        cbLanguage.addItem("German");
        ListenerKeyOverlayFirstType listenerKeyHold = new ListenerKeyOverlayFirstType(ProgramFrame.this);
        tfPhrase.addKeyListener(listenerKeyHold);
        setContentPane(mainPanel);
        setTitle("Password Generator");
        setSize(320, 470);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setVisible(true);

        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String passwordLength;

                // Если длина пароля не указана, то по дефолту она будет равна 10
                if ((passwordLength = thPasswordLength.getText()).equals("")) {
                    passwordLength = "10";
                }

                checkLanguage();
                alphabet.addNumbers(cbNumbers.isSelected());
                alphabet.addUpperCase(cbUpperCase.isSelected());
                alphabet.addPunctuationMarks(cbPunctuationMarks.isSelected());


                taPassword1.setText(passwordGenerator.generatePassword(Integer.parseInt(passwordLength), alphabet));
                alphabet = new EnglishAlphabet();
            }
        });
        jButton2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                // Обнуление счетчика
                listenerKeyHold.resetTheCounter();
                tfPhrase.setText("");
                taKeyHold.setText("");
            }
        });

        cbUpperCase.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

            }
        });
    }

    private void checkLanguage() {
        if (cbLanguage.getSelectedIndex() == 0) {
            alphabet = new EnglishAlphabet();
        } else if (cbLanguage.getSelectedIndex() == 1) {
            alphabet = new GermanAlphabet(alphabet);
        }
    }

}

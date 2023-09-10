
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.time.LocalTime;

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
    private JCheckBox cbSpecialSigns;
    private JCheckBox cbNumbers;
    private JTextField thPasswordLength;
    private JButton jButton2;
    private final PasswordService passwordService = new PasswordService();

    public void showKeyHold(String averageKeyHold) {
        taKeyHold.setText(averageKeyHold);
    }

    public ProgramFrame() {
        KeysListener keysListener = new KeysListener(ProgramFrame.this);
        tfPhrase.addKeyListener(keysListener);
        setContentPane(mainPanel);
        setTitle("Password Generator");
        setSize(320, 450);
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
                String str = passwordService.generatePassword(Integer.parseInt(passwordLength), cbNumbers.isSelected(), cbSpecialSigns.isSelected(), cbUpperCase.isSelected());
                taPassword1.setText(str);
            }
        });
        jButton2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                // Обнуление счетчика
                keysListener.resetTheCounter();
                tfPhrase.setText("");
                taKeyHold.setText("");
            }
        });
    }
}

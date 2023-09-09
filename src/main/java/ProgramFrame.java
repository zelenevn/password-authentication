import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.Calendar;
import java.util.Date;
import java.util.Locale;

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
    private long[] averageRetentionTime = {0, 0};
    private Long initialTime;

    private final KeyListener listener = new KeyListener() {
        @Override
        public void keyTyped(KeyEvent keyEvent) {
        }

        @Override
        public void keyPressed(KeyEvent keyEvent) {
            if (initialTime == null) {
                initialTime = LocalTime.now().toNanoOfDay();
                System.out.println(initialTime);
                System.out.println(1);
            }
        }

        @Override
        public void keyReleased(KeyEvent keyEvent) {
            System.out.println(2);
            averageRetentionTime[0]++;
            averageRetentionTime[1] += (LocalTime.now().toNanoOfDay() - initialTime) / 1000000;
            taKeyHold.setText(String.valueOf(averageRetentionTime[1]/averageRetentionTime[0]));
            initialTime = null;
        }
    };

    public ProgramFrame() {
        tfPhrase.addKeyListener(listener);
        setContentPane(mainPanel);
        setTitle("Password Generator");
        setSize(320, 450);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setVisible(true);

        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String passwordLength;
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
                averageRetentionTime = new long[]{0, 0};
                tfPhrase.setText("");
                taKeyHold.setText("");
            }
        });
    }
}

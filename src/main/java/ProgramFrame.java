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
    private long[] averageRetentionTime = {0, 0};
    // в нулевом индексе количество нажатий
    // в первом общее время удержания в мс
    private Long initialTime;

    // Слушатель клавиш
    private final KeyListener listener = new KeyListener() {
        @Override
        public void keyTyped(KeyEvent keyEvent) {
        }

        /**
         * Метод обрабатывает нажатие клавиши.
         *
         * @param keyEvent the event to be processed
         */
        @Override
        public void keyPressed(KeyEvent keyEvent) {

            // Сохраняем нс нажатии клавиши в initialTime
            if (initialTime == null) {
                initialTime = LocalTime.now().toNanoOfDay();
            }
        }

        /**
         * Метод обрабатывает отпускание клавиши.
         *
         * @param keyEvent the event to be processed
         */
        @Override
        public void keyReleased(KeyEvent keyEvent) {
            // Добавление в averageRetentionTime[0] нажатие клавиши
            averageRetentionTime[0]++;

            // Добавление в averageRetentionTime[1] мс удержания клавиши
            averageRetentionTime[1] += (LocalTime.now().toNanoOfDay() - initialTime) / 1000000;

            // Вывод в taKeyHold среднего времени удержания клавиш
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
                averageRetentionTime = new long[]{0, 0};
                tfPhrase.setText("");
                taKeyHold.setText("");
            }
        });
    }
}

package domain;

import gui.ProgramFrame;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.time.LocalTime;
import java.util.HashMap;

public class KeysListener implements KeyListener {
    private final ProgramFrame programFrame;
    private long[] averageRetentionTime = {0, 0};
    // в нулевом индексе количество нажатий
    // в первом общее время удержания в мс
    private final HashMap<Character, Long> hashMap = new HashMap<>();

    public KeysListener(ProgramFrame programFrame) {
        this.programFrame = programFrame;
    }

    public void resetTheCounter() {
        averageRetentionTime = new long[]{0, 0};
    }

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

        // Сохраняем нс нажатии клавиши в мапу
        if (!hashMap.containsKey(keyEvent.getKeyChar())) {
            hashMap.put(keyEvent.getKeyChar(), LocalTime.now().toNanoOfDay());
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
        averageRetentionTime[1] += (LocalTime.now().toNanoOfDay() - hashMap.remove(keyEvent.getKeyChar())) / 1000000;

        // Вывод в taKeyHold среднего времени удержания клавиш
        programFrame.showKeyHold(String.valueOf(averageRetentionTime[1] / averageRetentionTime[0]));
    }
}

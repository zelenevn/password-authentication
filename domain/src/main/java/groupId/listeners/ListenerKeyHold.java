package groupId.listeners;

import groupId.ProgramFrame;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.time.LocalTime;
import java.util.HashMap;
import java.util.Map;

public class ListenerKeyHold implements KeyListener {
    private final ProgramFrame programFrame;
    private long[] averageRetentionTime = {0, 0};
    // в нулевом индексе количество нажатий
    // в первом общее время удержания в мс
    private final Map<Character, Long> pressingKeys;

    public ListenerKeyHold(ProgramFrame programFrame) {
        this.programFrame = programFrame;
        this.pressingKeys = new HashMap<>();
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
     * @param keyEvent событие, подлежащее обработке
     */
    @Override
    public void keyPressed(KeyEvent keyEvent) {

        // Сохраняем нс нажатии клавиши в мапу
        if (!pressingKeys.containsKey(keyEvent.getKeyChar())) {
            pressingKeys.put(keyEvent.getKeyChar(), LocalTime.now().toNanoOfDay());
        }
    }

    /**
     * Метод обрабатывает отпускание клавиши.
     *
     * @param keyEvent событие, подлежащее обработке
     */
    @Override
    public void keyReleased(KeyEvent keyEvent) {
        // Добавление в averageRetentionTime[0] нажатие клавиши
        averageRetentionTime[0]++;

        // Добавление в averageRetentionTime[1] мс удержания клавиши
        averageRetentionTime[1] += (LocalTime.now().toNanoOfDay() - pressingKeys.remove(keyEvent.getKeyChar())) / 1000000;

        // Вывод в taKeyHold среднего времени удержания клавиш
        programFrame.showKeyHold(String.valueOf(averageRetentionTime[1] / averageRetentionTime[0]));
    }
}

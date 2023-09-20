package groupId.listeners;

import groupId.ProgramFrame;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class ListenerOverlayKey implements KeyListener {
    private final ProgramFrame programFrame;
    private Character clampedKey = 0;
    private int numberOverlays = 0;

    public ListenerOverlayKey(ProgramFrame programFrame) {
        this.programFrame = programFrame;
    }

    public void resetTheCounter() {
        numberOverlays = 0;
    }

    @Override
    public void keyTyped(KeyEvent e) {

    }

    /**
     * Метод обрабатывает нажатие клавиши.
     *
     * @param e событие, подлежащее обработке
     */
    @Override
    public void keyPressed(KeyEvent e) {
        // Сохраняем клавишу
        if (clampedKey == 0) {
            clampedKey = e.getKeyChar();
        }
    }

    /**
     * Метод обрабатывает отпускание клавиши.
     *
     * @param e событие, подлежащее обработке
     */
    @Override
    public void keyReleased(KeyEvent e) {

        // Если отпущенная клавиша не равна первой нажатой клавиши
        // то, к числу наложений добавляем единицу
        // и выводим число наложений в приложение
        if (clampedKey != e.getKeyChar()) {
            numberOverlays++;
            programFrame.showKeyHold(String.valueOf(numberOverlays));
        } else if (clampedKey == e.getKeyChar()) {
            clampedKey = 0;
        }
    }
}

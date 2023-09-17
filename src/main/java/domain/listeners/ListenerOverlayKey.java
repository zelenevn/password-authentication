package domain.listeners;

import gui.ProgramFrame;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.time.LocalTime;
import java.util.HashMap;

public class ListenerOverlayKey implements KeyListener {
    private final ProgramFrame programFrame;

    public ListenerOverlayKey(ProgramFrame programFrame) {
        this.programFrame = programFrame;
    }

    private Character clampedKey = 0;
    private int numberOverlays = 0;

    public void resetTheCounter() {
        numberOverlays = 0;
    }

    @Override
    public void keyTyped(KeyEvent e) {

    }

    /**
     * Метод обрабатывает нажатие клавиши.
     *
     * @param e the event to be processed
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
     * @param e the event to be processed
     */
    @Override
    public void keyReleased(KeyEvent e) {

        // Если отпущенная клавиша не равна первой нажатой клавиши
        // то, к числу наложений добавляем единицу
        // и выводим число наложений в приложение
        if (clampedKey != e.getKeyChar()){
            numberOverlays++;
            programFrame.showKeyHold(String.valueOf(numberOverlays));
        }else if (clampedKey == e.getKeyChar()){
            clampedKey = 0;
        }
    }
}

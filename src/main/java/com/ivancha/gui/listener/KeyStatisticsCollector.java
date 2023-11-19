package com.ivancha.gui.listener;

import lombok.Getter;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.List;


public class KeyStatisticsCollector implements KeyListener {

    @Getter
    private final List<Long> timeBetweenPresses = new ArrayList<>();
    @Getter
    private final List<Long> pressTimeList = new ArrayList<>();

    private boolean isKeyPressed = false;
    private long startPressFreeTime = System.currentTimeMillis();
    private long startPressTime;

    public void keyTyped(KeyEvent e) {

        if (!isKeyPressed) {

            long nowTime = System.currentTimeMillis();

            startPressTime = nowTime;
            timeBetweenPresses.add(nowTime - startPressFreeTime);
            isKeyPressed = true;
        }
    }

    public void keyReleased(KeyEvent e) {

        if (isKeyPressed) {

            long nowTime = System.currentTimeMillis();

            pressTimeList.add(nowTime - startPressTime);
            startPressFreeTime = nowTime;
            isKeyPressed = false;
        }
    }

    public void keyPressed(KeyEvent e) {}


    public void clear() {
        timeBetweenPresses.clear();
        pressTimeList.clear();
    }
}

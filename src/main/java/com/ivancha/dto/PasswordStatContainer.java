package com.ivancha.dto;

import java.util.Map;


public interface PasswordStatContainer {

    Map<Integer, Integer> timeBetweenPresses();

    Map<Integer, Integer> keyPressTime();

    String value();
}

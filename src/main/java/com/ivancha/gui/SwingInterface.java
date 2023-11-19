package com.ivancha.gui;

import com.ivancha.gui.window.PasswordFrame;

import static com.ivancha.service.ServiceUtil.startServices;


public class SwingInterface {


    public static void main(String[] args) {

        var serviceResources = startServices();

        var frame = new PasswordFrame(serviceResources);
        frame.setVisible(true);
    }










}


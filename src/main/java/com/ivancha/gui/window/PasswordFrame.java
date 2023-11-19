package com.ivancha.gui.window;

import com.ivancha.service.ServiceUtil.ServiceResources;
import com.ivancha.util.HibernateUtil;

import javax.swing.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;


public class PasswordFrame extends JFrame {


    public PasswordFrame(ServiceResources sr) {

        super("Пароли, парольчики, паролища");

        JPanel regPanel = new RegistrationPanel(sr.userService(), sr.passwordService());
        this.getContentPane().add(regPanel);

        this.pack();
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        this.addWindowListener(new WindowAdapter() {

            @Override
            public void windowClosing(WindowEvent e) {
                HibernateUtil.closeSessionFactory();
            }
        });
    }
}

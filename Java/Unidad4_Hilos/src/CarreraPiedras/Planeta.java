/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CarreraPiedras;

import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.Icon;
import javax.swing.JLabel;

/**
 *
 * @author wolfteinter
 */
public class Planeta extends JLabel implements Runnable{
    private JLabel label;
    private int distancia;
    public long time;
    public  Planeta(JLabel label){
        this.label=label;
    }

    public long getTime() {
        return time;
    }
    
    @Override
    public void run() {
        Random ran = new Random();
        long timpI = System.currentTimeMillis();
        for(int i=label.getX();i<776;i++){
            label.setLocation(i,label.getY());
            try {
                Thread.sleep(ran.nextInt(100));
            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
        }
        time = System.currentTimeMillis()-timpI;
    }
    
}

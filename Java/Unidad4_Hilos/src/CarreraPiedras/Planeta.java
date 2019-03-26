/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package CarreraPiedras;

import javax.swing.Icon;
import javax.swing.JLabel;

/**
 *
 * @author wolfteinter
 */
public class Planeta extends JLabel implements Runnable{
    private JLabel label;
    private int distancia;
    Thread hilo;
    public void Planeta(JLabel label,String ruta){
        this.label=label;
        this.distancia = distancia;
        hilo = new Thread(this);
    }
    @Override
    public void run() {
        for(int i=label.getX();i<this.distancia;i++){
            label.setLocation(i,label.getY());
        }
    }
    
}

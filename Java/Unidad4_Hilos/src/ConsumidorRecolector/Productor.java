/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ConsumidorRecolector;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author wolfteinter
 */
public class Productor extends Thread{
    private Contenedor contenedor;
    public Productor(Contenedor c,String n){
        super(n);
        contenedor = c;
    }
    @Override
    public void run(){
        for(int i=0;i<=10;i++){
            try {
                contenedor.poner(i);
                System.out.println(getName()+" Produce: "+i);
                Thread.sleep(1000);
            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
        }
    }
}

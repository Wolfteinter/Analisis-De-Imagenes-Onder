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
public class Contenedor {
    private int dato;
    private boolean hayDato = false;
    public synchronized void poner(int d){
        while(this.hayDato){
            try{
                wait();
            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
        
        }
        dato=d;
        hayDato=true;
        notifyAll();
    }
    
    public synchronized int sacar(){
        while(!hayDato){
            try {
                wait();
            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
        }
        hayDato=false;
        notifyAll();
        return dato;
    }
}

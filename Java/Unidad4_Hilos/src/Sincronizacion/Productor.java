/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Sinclonizacion;

import java.util.Arrays;
import java.util.Random;

/**
 *
 * @author wolfteinter
 */
public class Productor extends Thread{
    Contenedor contenedor;
    public Productor(Contenedor contenedor) {
        this.contenedor = contenedor;
    }
    public void run(){
        Random r = new Random();
        int ans;
            while(true){
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException ex) {
                    ex.printStackTrace();
                }
                ans = r.nextInt(10)+1;
                contenedor.poner(ans);
                //System.out.println(Arrays.toString(contenedor.buffer));
                System.out.println("Puse: "+ans);
            }
    }
    
}

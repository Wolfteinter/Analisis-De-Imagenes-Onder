/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Sinclonizacion;

import java.util.Arrays;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author wolfteinter
 */
public class Consumidor extends Thread{
    Contenedor contenedor;
    public Consumidor(Contenedor contenedor) {
        this.contenedor = contenedor;
    }
    public void run(){
            while(true){
                System.out.println("Saque: "+contenedor.sacar());
            }
    }
    
}
    


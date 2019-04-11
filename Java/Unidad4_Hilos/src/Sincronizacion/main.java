/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Sinclonizacion;

import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author wolfteinter
 */
public class main {
    public static void main(String args[]){
        Contenedor contenedor = new Contenedor(20);
        Productor productor = new Productor(contenedor);
        Consumidor consumidor = new Consumidor(contenedor);
        productor.start();
        consumidor.start();
        
        
    }
}

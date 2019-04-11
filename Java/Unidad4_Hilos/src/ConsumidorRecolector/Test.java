/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ConsumidorRecolector;

/**
 *
 * @author wolfteinter
 */
public class Test {
    public static void main(String[] args) {
        Contenedor c = new Contenedor();
        Productor p1 = new Productor(c,"Jaime");
        Productor p2 = new Productor(c,"Aparacio");
        Consumidor c1 = new Consumidor(c,"Juanito");
        Consumidor c2 = new Consumidor(c,"Luis");
        Consumidor c3 = new Consumidor(c,"Chano");
        Consumidor c4 = new Consumidor(c,"Pedro");
        Consumidor c5 = new Consumidor(c,"Alan");
        p1.start();
        p2.start();
        c1.start();
        c2.start();
        c3.start();
        c4.start();
        c5.start();
    }
}

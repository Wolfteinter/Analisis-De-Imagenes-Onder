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
public class Consumidor extends Thread{
    private Contenedor contenedor;
    public Consumidor(Contenedor c,String n){
        super(n);
        contenedor = c;
    }
    @Override
    public void run(){
        int val = 0;
        for(int i=0;i<=10;i++){
           val = contenedor.sacar();
            System.out.println(getName()+" Consume: "+val);
        }
    }
}

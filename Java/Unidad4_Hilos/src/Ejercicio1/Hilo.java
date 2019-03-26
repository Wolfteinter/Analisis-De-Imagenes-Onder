/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio1;

/**
 *
 * @author wolfteinter
 */
public class Hilo extends Thread{
    private int num;
    private String nombre;
    public Hilo(int n,String nombre){
        this.num=n;
        this.nombre=nombre;
        this.setName(nombre);
    }
    @Override
    public void run(){
        for(int i=0;i<this.num;i++){
            System.out.println(i +" _ "+this.getName());
        }
    }
    
    public static void main(String[] args) {
        Hilo hi = new Hilo(15,"Onder");//Creando el hilo 
        Hilo h2 = new Hilo(15,"Pancho");//Creando el hilo 
        hi.start();
        h2.start();
    }
}

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
public class hilo2 implements Runnable{
    private int num;
    private String name;
    public hilo2(int n,String g){
        this.num = n;
        this.name = g;
    }
    @Override
    public void run() {
        for (int i=0;i<this.num;i++) {
            System.out.println(i+" "+name);
        }
    }
    public static void main(String[] args) {
        hilo2 hilo = new hilo2(20,"Onder");
        hilo2 hilo2 = new hilo2(20,"Francisco");
        Thread t1 = new Thread(hilo);
        Thread t2 = new Thread(hilo2);
        t1.start();
        t2.start();
    }
    
}

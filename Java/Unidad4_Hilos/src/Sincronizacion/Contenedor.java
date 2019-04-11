/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Sinclonizacion;

/**
 *
 * @author wolfteinter
 */
public class Contenedor {
    int buffer[];
    int contador;
    int tam;
    public Contenedor(int tam){
        this.tam=tam;
        this.contador = 0;
        buffer = new int[tam];
    }
    public synchronized void poner(int obj){
        while(contador>=tam){
            try{
                wait();
            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
        
        }
        if(contador<=tam){
            this.buffer[contador]=obj;
            this.contador++;
            notifyAll();
        }
    }
    public synchronized int sacar(){
        while(contador==0){
            try{
                wait();
            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
        
        }
        if(contador<=tam){
                    int ans;
        ans = this.buffer[contador-1];
        contador--;
        notifyAll();
        return ans;
        }
        return 0;
    }
}

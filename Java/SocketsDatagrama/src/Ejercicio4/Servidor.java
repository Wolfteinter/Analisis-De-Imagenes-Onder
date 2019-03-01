/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio4;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.SocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.DatagramChannel;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author wolfteinter
 */
public class Servidor {
    private DatagramChannel canal;
    private ByteBuffer buffer;
    private int port = 5000;
    public Servidor(){
        try {
            canal=DatagramChannel.open();
            canal.configureBlocking(false);
            InetSocketAddress isa = new InetSocketAddress("127.0.0.1",this.port);
            canal.bind(isa);
            System.out.println("Servidor activo en: "+isa);
            
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
    public void recibir(){
        try {
            while(true){
       
                if(buffer == null){
                    Thread.sleep(4000);
                }else{
                    
                    buffer = ByteBuffer.allocate(1024);
                    SocketAddress sa = canal.receive(buffer);
                    System.out.println(new String(buffer.array()));
                    //Preparar para lectura 
                    buffer.flip();
                    canal.send(buffer, sa);
                    canal.close();
                }
               
            }
            
            
            
        } catch (IOException ex) {
            ex.printStackTrace();
        } catch (InterruptedException ex) {
            Logger.getLogger(Servidor.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    public static void main(String[] args) {
        Servidor s = new Servidor();
        s.recibir();
    }
    
}

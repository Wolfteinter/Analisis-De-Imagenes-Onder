/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio4;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.DatagramChannel;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author wolfteinter
 */
public class Cliente {
    private DatagramChannel canal;
    private ByteBuffer buffer;
    private String ip = "127.0.0.1";
    private int port = 5000;
    public Cliente(){
        try {
            canal = DatagramChannel.open();
            canal.configureBlocking(false);
            InetSocketAddress isa = new InetSocketAddress(ip,port);
            canal.bind(null);
            System.out.println("Cliente activo");
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        
    }
    public void enviar(String msg){
        try {
            buffer=ByteBuffer.wrap(msg.getBytes());
            canal.send(buffer,canal.getLocalAddress());
            buffer.clear();
            canal.receive(buffer);
            System.out.println(new String(buffer.array()));
            canal.close();
            
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        
    }
    public static void main(String[] args) {
        Cliente c = new Cliente();
        c.enviar("Hola a todos");
        
    }
}

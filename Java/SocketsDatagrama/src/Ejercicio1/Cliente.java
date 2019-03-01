/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio1;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.SocketException;

/**
 *
 * @author wolfteinter
 */
public class Cliente {
    private DatagramSocket cliente;
    private DatagramPacket recibido;
    private DatagramPacket enviar;
    public Cliente(){
        try {
            this.cliente=new DatagramSocket();
        } catch (SocketException ex) {
            ex.printStackTrace();
        }
    }
    public void recibir(){
        try {
            byte buffer[] = new byte[1024];
            this.recibido = new DatagramPacket(buffer,buffer.length);
            cliente.receive(recibido);
            System.out.println(new String(recibido.getData()));
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
    public void enviar(){
        try {
            byte buffer[] = "Hola Servidor".getBytes();
            this.enviar = new DatagramPacket(buffer,buffer.length,InetAddress.getByName("127.0.0.1"),5500);
            cliente.send(enviar);
        }catch (IOException ex) {
            ex.printStackTrace();
        }
    }
    public static void main(String[] args) {
        Cliente s = new Cliente();
        s.enviar();
        s.recibir();

    }

}

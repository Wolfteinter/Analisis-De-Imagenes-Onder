/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio1;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author wolfteinter
 */
public class Servidor {

    private DatagramSocket servidor;
    private DatagramPacket recibido;
    private DatagramPacket enviar;
    private int puerto;

    public Servidor(int port) {
        this.puerto = port;
        try {
            this.servidor = new DatagramSocket(puerto);
        } catch (SocketException ex) {
            ex.printStackTrace();
        }
    }

    public void recibir() {
        try {
            byte buffer[] = new byte[1024];
            this.recibido = new DatagramPacket(buffer, buffer.length);
            servidor.receive(recibido);
            System.out.println(new String(recibido.getData()));
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public void enviar() {
        try {
            byte buffer[] = "Hola cliente".getBytes();
            this.enviar = new DatagramPacket(buffer, buffer.length, recibido.getAddress(), recibido.getPort());
            servidor.send(enviar);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public static void main(String[] args) {
        Servidor s = new Servidor(5500);
        s.recibir();
        s.enviar();
    }

}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio2;

import Ejercicio3.*;
import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author wolfteinter
 */
public class Cliente {
    private DatagramSocket socket;
    private DatagramPacket envio;
    private DatagramPacket recibo;
    private int npaq;
    private File myFile;
    private BufferedInputStream bis;

    public Cliente(String nombre) {
        try {
            socket = new DatagramSocket();
            myFile = new File(nombre);
            bis = new BufferedInputStream(new FileInputStream(myFile));
                    
        } catch (SocketException ex) {
            ex.printStackTrace();
        } catch (FileNotFoundException ex) {
           ex.printStackTrace();
        }
    }
    public void enviarArchivo(){
        //duada sobre el numero de paquetes 
        npaq = (int) Math.ceil(((double)myFile.length()/1024));
        System.out.println(npaq);
        for(int i=0;i<npaq;i++){
             byte buffer[] = new byte[1024];
            try {
                bis.read(buffer,0,buffer.length);
                System.out.println("Paquetenum: "+(i+1));
                envio = new DatagramPacket(buffer,buffer.length,InetAddress.getByName("127.0.0.1"),1234);
                socket.send(envio);
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
        try {
            bis.close();
        } catch (IOException ex) {
            Logger.getLogger(Cliente.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    public static void main(String[] args) {
        Cliente n = new Cliente("IPN.png");
        n.enviarArchivo();
    }
    
}

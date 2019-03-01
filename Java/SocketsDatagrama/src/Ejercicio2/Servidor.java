/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio2;

import Ejercicio3.*;
import java.io.BufferedOutputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
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
    private DatagramPacket envio;
    private FileOutputStream fos;
    private BufferedOutputStream bos;

    public Servidor(int port){
        try {
            servidor = new DatagramSocket(port);
        } catch (SocketException ex) {
            Logger.getLogger(Servidor.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    public void recibirArchivo(String nombre){
        try {
            fos = new FileOutputStream(nombre);
            bos = new BufferedOutputStream(fos);
            byte buffer[] = new byte[1024];
            recibido = new DatagramPacket(buffer,buffer.length);
            do{
                servidor.receive(recibido);
                bos.write(recibido.getData(),0,recibido.getData().length);
            }while(recibido.getData().length == 1024);
        } catch (FileNotFoundException ex) {
            ex.printStackTrace();
        } catch (IOException ex) {
            ex.printStackTrace();
        }finally{
            try {
                fos.close();
                bos.close();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
            
        }
        
    }
    public static void main(String[] args) {
        Servidor s = new Servidor(1234);
        s.recibirArchivo("Nuevo.png");
    }
    
    
}

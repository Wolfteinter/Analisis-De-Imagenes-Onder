/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ServidorTelnet;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author wolfteinter
 */
class HiloCliente extends Thread{
    private Socket cliente;
     private PrintWriter salida;
     private BufferedReader entrada;
    public HiloCliente(Socket s){
        cliente=s;
    }
    public void run(){
        while(true){
            try {
                entrada = new BufferedReader(new InputStreamReader(cliente.getInputStream()));
                String respuesta = entrada.readLine();
                System.out.println("Respuesta: "+respuesta);
            } catch (IOException ex) {
              ex.printStackTrace();
            }
        }
        /*
        try {
            salida = new PrintWriter(cliente.getOutputStream());
            System.out.println("Cliente: "+cliente.getInetAddress().getHostName() +" Puerto: "+cliente.getPort());
            salida.print("Hola cliente");
        } catch (IOException ex) {
            ex.printStackTrace();
        }*/
    }
}

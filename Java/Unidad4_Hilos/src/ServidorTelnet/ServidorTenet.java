/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ServidorTelnet;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author wolfteinter
 */
public class ServidorTenet {
    private String ip;
    private int puerto;
    private ServerSocket serv;
    private Socket cliente;
    public ServidorTenet(int puerto){
        this.puerto = puerto;
        try {
            serv = new ServerSocket(puerto);
            escuchar();
            
        } catch (IOException ex) {
           ex.printStackTrace();
        }
    }

    private void escuchar() {
        while(true){
            try {
                cliente = serv.accept();
                //GESTION DE HILOS
                HiloCliente h = new HiloCliente(cliente);
                h.start();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
    }
    public static void main(String[] args) {
        ServidorTenet st = new ServidorTenet(1234);
        st.escuchar();
    }
}

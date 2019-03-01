/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicio5;

import java.io.IOException;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.NetworkInterface;
import java.net.StandardProtocolFamily;
import java.net.StandardSocketOptions;
import java.nio.ByteBuffer;
import java.nio.channels.DatagramChannel;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author wolfteinter
 */

public class ClienteMulticast {
private int port = 4321; 
private String ip = "230.0.0.0"; 
private DatagramChannel canal;
private ByteBuffer buffer;
private NetworkInterface interf;
public ClienteMulticast(){
    try {
        canal = DatagramChannel.open();
        canal.bind(null);
        interf = NetworkInterface.getByName("wlp2s0");
        canal.setOption(StandardSocketOptions.IP_MULTICAST_IF, interf);
        System.out.println(interf.getName()+" multicast: "+interf.supportsMulticast());
    } catch (IOException ex) {
       ex.printStackTrace();
    }
}
public void enviarMSG(String msg){
    try {
            buffer = ByteBuffer.wrap(msg.getBytes());
    InetSocketAddress isa = new InetSocketAddress(ip,port);
        canal.send(buffer, isa);
    } catch (IOException ex) {
       ex.printStackTrace();
    }finally{
        try {
            canal.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
    public static void main(String[] args) {
        ClienteMulticast mcst = new ClienteMulticast();
        mcst.enviarMSG("Hola soy onder y subi mi primer problema en omega ");
                
    }
}

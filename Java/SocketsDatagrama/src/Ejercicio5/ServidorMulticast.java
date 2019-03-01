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
import java.nio.channels.MembershipKey;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author wolfteinter
 */
public class ServidorMulticast {
    private int port = 4321; 
private String ip = "230.0.0.0"; 
private DatagramChannel canal;
private ByteBuffer buffer;
private NetworkInterface interf;
private MembershipKey key;
public ServidorMulticast(){
    try {
        canal = DatagramChannel.open(StandardProtocolFamily.INET);
        interf = NetworkInterface.getByName("wlp2s0");
        canal.bind(new InetSocketAddress(port));
        canal.setOption(StandardSocketOptions.SO_REUSEADDR,true);
        canal.setOption(StandardSocketOptions.IP_MULTICAST_IF, interf);
        key = canal.join(InetAddress.getByName(ip), interf);
        System.out.println("Grupo: "+key);
    } catch (IOException ex) {
       ex.printStackTrace();
    }
}
public void recibirMsg(){
        try {  
            System.out.println("ESperando mensajes");
            buffer = ByteBuffer.allocate(1024);
            canal.receive(buffer);
            buffer.flip();
            System.out.println(new String(buffer.array()));
            key.drop();
            canal.close();
            
        } catch (IOException ex) {
            Logger.getLogger(ServidorMulticast.class.getName()).log(Level.SEVERE, null, ex);
        }
}
    public static void main(String[] args) {
        ServidorMulticast smc = new ServidorMulticast();
        smc.recibirMsg();
    }


}

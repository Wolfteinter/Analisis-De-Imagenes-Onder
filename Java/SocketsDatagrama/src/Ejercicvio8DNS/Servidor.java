/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ejercicvio8DNS;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author wolfteinter
 */
public class Servidor {
    private DatagramPacket envio;
    private DatagramPacket recibe;
    private DatagramSocket datagramSocket;
    private int puerto=5500;
    private ArrayList<String>[] Ips;
    private URL[] URLs;
    public Servidor(){
        URLs = new URL[100000000];
        Ips = new ArrayList[100000000];
                this.puerto = puerto;
        try {
            this.datagramSocket = new DatagramSocket(puerto);
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
    private int calcularHashCode(String url){
        int suma=0;
        for(int i=0;i<url.length();i++){
            suma+=(int)(url.charAt(i))*Math.pow(5,i);
        }
        return suma%100000000;
    }
    //Para añadir un Dominio 
    public void agregarDireccion(URL url,String ip){
        int hashIp=calcularHashCode(ip);
        int hashUrl=calcularHashCode(url.toString());
        if(URLs[hashIp]==null){
           URLs[hashIp] = url;
        }else{
            System.out.println("ya existe");
        }
        if(Ips[hashUrl]==null){
            Ips[hashUrl] = new ArrayList<String>();
            Ips[hashUrl].add(ip);
        }else{
            Ips[hashUrl].add(ip);
        }
    }
    //Busca 
    private String buscarURL(String ip){
        int hashIp=calcularHashCode(ip);
        if(URLs[hashIp]!=null){
          return URLs[hashIp].toString();  
        }
        System.out.println("No encontrada");
        return "error://desconocida/ninguna.er";
    }
    private String buscarIP(URL url){
        int hashUrl=calcularHashCode(url.toString());
        if(Ips[hashUrl]!=null){
          return Arrays.toString(Ips[hashUrl].toArray());  
        }
        System.out.println("No encontrada");
        return "No encontrada";
    }
    // El cliente envia una ip y el servidor la resulve enviandole la url
    public void resolverIP() {
        //Buscar el el hash 
        
        byte buffer[] = buscarURL(recibirIPs()).getBytes();
        try {
            // Instanciamos el envío
            this.envio = new DatagramPacket(buffer, buffer.length, 
                InetAddress.getLocalHost(), this.puerto);
            // Enviamos la petición
            this.datagramSocket.send(envio);
            // Construimos la URL
        }
        catch (MalformedURLException | UnknownHostException ex) {
            ex.printStackTrace();
        }
        catch (IOException ex) {
            ex.printStackTrace();
        }
    }
    private String recibirIPs() {
         String ips="";
        // Vamos a recibir un string con las direcciones IP
        byte buffer[] = new byte[2048];
        this.recibe = new DatagramPacket(buffer, buffer.length);
        try {
            this.datagramSocket.receive(this.recibe);
            String datos = new String(this.recibe.getData());
            System.out.println("IP resivida : "+datos);
            //El hash sale como 0 
            System.out.println("El del cliente : "+calcularHashCode(datos.replace((char)0,' ')));
            ips=datos.replace((char)0,' ');
        }
        catch (Exception e) {
            e.printStackTrace();
        }
        return ips;
    }
    //El cliente envia un dominio 
   public void resolverDominio() {
        try {
            // Obtenemos la representación del dominio
            byte buffer[] = buscarIP(new URL(recibirDominio())).getBytes();
            try {
                // Instanciamos el envío
                this.envio = new DatagramPacket(buffer, buffer.length,
                        InetAddress.getLocalHost(), this.puerto);
                // enviamos
                this.datagramSocket.send(this.envio);
                // recibimos el grupo de ips
            }
            catch (UnknownHostException ex) {
                ex.printStackTrace();
            }
            catch (IOException ex) {
                ex.printStackTrace();
            }
        }
        catch (MalformedURLException ex) {
            Logger.getLogger(Servidor.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    public String recibirDominio() {
        String mensaje = "error://desconocida/ninguna.er";
        //Creamos un buffer de tamaño 2048 bytes
        byte buffer[] = new byte[2048];
        this.recibe = new DatagramPacket(buffer, buffer.length);
        try {
            this.datagramSocket.receive(this.recibe);
            mensaje = new String(this.recibe.getData());
        }
        catch (IOException ex) {
            ex.printStackTrace();
        }
        return mensaje;
    }
    public static void main(String[] args) throws MalformedURLException {
        Servidor s =  new Servidor();
        URL url = new URL("http://www.google.com");
        s.agregarDireccion(url,"192.168.12.13");
        System.out.println("El del servidor : "+s.calcularHashCode("192.168.12.13"));
        System.out.println(s.buscarURL("192.168.12.13"));
        s.resolverIP();
        s.resolverDominio();
    }
    

    
}

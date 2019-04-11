/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package DetectorMasas;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.image.BufferedImage;

/**
 *
 * @author wolfteinter
 */
public class Tools {
    public static BufferedImage toBufferedImage (Image imagen){
         // imagen es un objeto de tipo BufferedImage
        if (imagen instanceof BufferedImage){
          return (BufferedImage)imagen;
        }
        BufferedImage bi = 
                new BufferedImage(imagen.getWidth(null), imagen.getHeight(null), BufferedImage.TYPE_INT_RGB);
        
        Graphics2D nueva = bi.createGraphics();
        nueva.drawImage(imagen, 0, 0,null);
        nueva.dispose();
        
        return bi;
    }
    public static Image toImage (BufferedImage bi){
        return bi.getScaledInstance(bi.getWidth(),bi.getHeight(), BufferedImage.TYPE_INT_RGB);
    }
       public static Image umbralizacionSimple(int u, Image imagenOriginal){
        BufferedImage bi = toBufferedImage(imagenOriginal);
        // recorremos el buffer
        for(int x=0; x<bi.getWidth();x++){
            for(int y=0;y<bi.getHeight();y++){
                Color color = new Color(bi.getRGB(x, y));
                int prom = (color.getRed()+color.getGreen()+color.getBlue())/3;
                if(prom<u){color = new Color(0, 0, 0);}
                else{
                color = new Color(255, 255, 255);
                }
                bi.setRGB(x, y,color.getRGB());       
            }
       }
       
       int meanX=1;
       int meanY=1;
       int pixelsC=0;
       for(int x=0; x<bi.getWidth();x++){
            for(int y=0;y<bi.getHeight();y++){
                Color color = new Color(bi.getRGB(x, y));
                if(color.getRed() == 0 && color.getGreen() == 0 && color.getBlue() == 0){
                    meanX+=x;
                    meanY+=y;
                    pixelsC++;
                }
            }
       }
       
       meanX = (int)meanX/pixelsC;
       meanY = (int)meanY/pixelsC;
       Color color = new Color(0,255,0);
       //bi.setRGB(meanX,meanY,color.getRGB());
       for(int x=meanX-5; x< meanX+5;x++){
            for(int y=meanY-5;y<meanY+5;y++){
                    bi.setRGB(x, y,color.getRGB());
            }
       }
       
       
       return toImage(bi);
    }
}

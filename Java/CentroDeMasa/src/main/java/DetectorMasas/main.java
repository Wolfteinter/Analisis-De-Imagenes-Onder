/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package DetectorMasas;

import com.github.sarxos.webcam.Webcam;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;

/**
 *
 * @author wolfteinter
 */
public class main {
    public static void main(String ars[]){
        Webcam webcam = Webcam.getDefault();
        webcam.open();
    }
    
}

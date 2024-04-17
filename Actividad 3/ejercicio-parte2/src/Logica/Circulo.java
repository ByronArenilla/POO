
package Logica;


public class Circulo {
    //Atributos
    int radio;
    //Constructor
    public Circulo(int radio) {
        this.radio = radio;
    }
    
    //Métodos
    public double calcularArea(){
        return Math.PI*Math.pow(radio, 2);
        
    }
    
    public double calcularPerimetro(){
        return 2*Math.PI*radio;
    }

}


package Logica;


public class Cuadrado {
    //Atributos
    int lado;
    
    
    //Constructores

    public Cuadrado(int lado) {
        this.lado = lado;
    }
    
    
    //Métodos
    public double calcularArea(){
        return lado*lado;
    }
    
    public double calcularPerimetro(){
        return(4*lado);
    }

}

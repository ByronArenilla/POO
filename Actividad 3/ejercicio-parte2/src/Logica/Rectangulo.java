
package Logica;


public class Rectangulo {
    //Atributos
    int base;
    int altura;
    
    //Constructor

    public Rectangulo(int base, int altura) {
        this.base = base;
        this.altura = altura;
    }
    
    //Métodos
    public double calcularArea(){
        return base*altura;
    }
    
    public double calcularPerimetro(){
        return (2*base)+(2*altura);
    }
    

}

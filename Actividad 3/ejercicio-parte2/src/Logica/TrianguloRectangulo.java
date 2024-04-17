
package Logica;


public class TrianguloRectangulo {
    //Atributos
    int base;
    int altura;
    
    //Constructor

    public TrianguloRectangulo(int base, int altura) {
        this.base = base;
        this.altura = altura;
    }
    
    public double CalcularArea(){
        return (base * altura/2);
    }
    
    public double calcularPerimetro(){
        return(base+altura+calcularHipotenusa());
    }
    
    public double calcularHipotenusa(){
        return Math.pow(base*base + altura * altura,0.5);
    }
    
    public String determinarTriangulo(){
        if ((base == altura) && (base == calcularHipotenusa())&& (altura == calcularHipotenusa())){
            return "Es un triangulo equilátero";
        }else if ((base != altura)&&(base!= calcularHipotenusa())&& (altura!= calcularHipotenusa())){
            return "Es un triangulo escaleno";
        }else{
            return "Es un triangulo isosceles";
        }           
    }

}

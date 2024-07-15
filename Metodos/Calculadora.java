package Metodos;

public class Calculadora {

    public static void main(String[] args) {
        int resultadoSoma = CalcularMetodos.somar(5, 3);
        int resultadoSomaTresNumeros = CalcularMetodos.somar(5, 3, 2);
        int resultadoSubtracao = CalcularMetodos.subtrair(10, 4);
        int resultadoMultiplicacao = CalcularMetodos.multiplicar(5, 7);
        
        // Aqui vamos lidar com a exceção caso haja divisão por zero
        try {
            double resultadoDivisao = CalcularMetodos.dividir(10, 2);
            System.out.println("Resultado da soma: " + resultadoSoma);
            System.out.println("Resultado da soma de três números: " + resultadoSomaTresNumeros);
            System.out.println("Resultado da subtração: " + resultadoSubtracao);
            System.out.println("Resultado da multiplicação: " + resultadoMultiplicacao);
            System.out.println("Resultado da divisão: " + resultadoDivisao);
        } catch (IllegalArgumentException e) {
            System.out.println("Erro ao dividir: " + e.getMessage());
        }
    }
}

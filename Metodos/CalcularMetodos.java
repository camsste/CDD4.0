package Metodos;

public class CalcularMetodos {

    public static int somar(int a, int b) {
        return a + b;
    }

    public static int somar(int a, int b, int c) {
        return a + b + c;
    }

    public static int subtrair(int a, int b) {
        return a - b;
    }

    public static int multiplicar(int a, int b) {
        return a * b;
    }

    public static double dividir(int a, int b) {
        if (b != 0) {
            return (double) a / b;
        } else {
            throw new IllegalArgumentException("Não é possível dividir por zero.");
        }
    }
}

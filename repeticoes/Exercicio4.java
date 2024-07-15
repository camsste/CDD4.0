package repeticoes;

public class Exercicio4 {

    public static void main(String[] args) {
        System.out.println("Números pares de 1 a 100:");
        int numeroPar = 2;
        while (numeroPar <= 100) {
            System.out.print(numeroPar + " ");
            numeroPar += 2;
        }
        System.out.println(); // Adiciona uma quebra de linha após os números pares

        System.out.println("\nNúmeros ímpares de 1 a 100:");
        int numeroImpar = 1;
        while (numeroImpar <= 100) {
            System.out.print(numeroImpar + " ");
            numeroImpar += 2;
        }
        System.out.println(); // Adiciona uma quebra de linha após os números ímpares
    }
}

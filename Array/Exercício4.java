package Array;

import java.util.Arrays;
import java.util.Scanner;

public class Exercício4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Insira os números separados por espaços: ");
        String input = scanner.nextLine().trim(); 

        String[] parts = input.split("\\s+"); 

        int[] numeros = new int[parts.length];

        try {
            for (int i = 0; i < parts.length; i++) {
                numeros[i] = Integer.parseInt(parts[i]);
            }
        } catch (NumberFormatException e) {
            System.err.println("Erro: Entrada inválida. Certifique-se de inserir apenas números separados por espaços.");
            System.exit(1); 
        }

        System.out.print("Array original: ");
        for (int num : numeros) {
            System.out.print(num + " ");
        }
        System.out.println();

        int[] invertido = new int[numeros.length];

        for (int i = 0; i < numeros.length; i++) {
            invertido[i] = numeros[numeros.length - 1 - i];
        }

        System.out.print("Array invertido: ");
        for (int num : invertido) {
            System.out.print(num + " ");
        }
        System.out.println();

        Arrays.sort(numeros);

        System.out.print("Array ordenado crescente: ");
        for (int num : numeros) {
            System.out.print(num + " ");
        }
        System.out.println();

        scanner.close();
    }
}

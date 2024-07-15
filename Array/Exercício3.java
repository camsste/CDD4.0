package Array;
import java.util.Scanner;

public class Exercício3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Pedir ao usuário para inserir os números
        System.out.print("Insira os números separados por espaços: ");
        String input = scanner.nextLine();

        // Dividir a entrada em números individuais
        String[] parts = input.split(" ");
        int[] numeros = new int[parts.length];

        // Converter os números de string para int e guardar no array 'numeros'
        for (int i = 0; i < parts.length; i++) {
            numeros[i] = Integer.parseInt(parts[i]);
        }

        // Imprimir o array original
        System.out.print("Array original: ");
        for (int num : numeros) {
            System.out.print(num + " ");
        }
        System.out.println();

        // Criar um novo array para guardar os números invertidos
        int[] invertido = new int[numeros.length];

        // Inverter o array 'numeros' e guardar em 'invertido'
        for (int i = 0; i < numeros.length; i++) {
            invertido[i] = numeros[numeros.length - 1 - i];
        }

        // Imprimir o array invertido
        System.out.print("Array invertido: ");
        for (int num : invertido) {
            System.out.print(num + " ");
        }
        System.out.println();

        scanner.close();
    }
}

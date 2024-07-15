package Array; // Definindo o pacote onde a classe está localizada

import java.util.Scanner; // Importando a classe Scanner do pacote java.util

public class Exercício1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Arrays para armazenar os valores digitados pelo usuário
        int[] arrayA = new int[10];
        int[] arrayB = new int[10];
        int[] arrayC = new int[10];
        int[] arrayD = new int[10];

        // Preenchendo Array A
        System.out.println("Digite os valores para o Array A (separados por espaço):");
        for (int i = 0; i < arrayA.length; i++) {
            arrayA[i] = scanner.nextInt();
        }

        // Preenchendo Array B
        System.out.println("Digite os valores para o Array B (separados por espaço):");
        for (int i = 0; i < arrayB.length; i++) {
            arrayB[i] = scanner.nextInt();
        }

        // Preenchendo Array C
        System.out.println("Digite os valores para o Array C (separados por espaço):");
        for (int i = 0; i < arrayC.length; i++) {
            arrayC[i] = scanner.nextInt();
        }

        // Preenchendo Array D
        System.out.println("Digite os valores para o Array D (separados por espaço):");
        for (int i = 0; i < arrayD.length; i++) {
            arrayD[i] = scanner.nextInt();
        }

        // Imprimindo os Arrays
        System.out.print("Array A: ");
        for (int i = 0; i < arrayA.length; i++) {
            System.out.print(arrayA[i] + " ");
        }
        System.out.println();

        System.out.print("Array B: ");
        for (int i = 0; i < arrayB.length; i++) {
            System.out.print(arrayB[i] + " ");
        }
        System.out.println();

        System.out.print("Array C: ");
        for (int i = 0; i < arrayC.length; i++) {
            System.out.print(arrayC[i] + " ");
        }
        System.out.println();

        System.out.print("Array D: ");
        for (int i = 0; i < arrayD.length; i++) {
            System.out.print(arrayD[i] + " ");
        }
        System.out.println();

        scanner.close();
    }
}

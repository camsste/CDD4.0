package Basico1;

import java.util.Scanner;

public class Exercicio5 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite a primeira nota: ");
        double nota1 = scanner.nextDouble();

        System.out.print("Digite a segunda nota: ");
        double nota2 = scanner.nextDouble();

        // Calculando a média das notas
        double media = (nota1 + nota2) / 2;

        // Exibindo o resultado
        System.out.println("A média das notas " + nota1 + " e " + nota2 + " é: " + media);

        scanner.close();
    }
}

package repeticoes;

import java.util.Scanner;

public class Exercicio1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Quantos alunos tem na sala? ");
        int numeroAlunos = scanner.nextInt();

        int contador = 1;
        double somaNotas = 0.0;

        while (contador <= numeroAlunos) {
            System.out.print("Digite a nota do aluno " + contador + ": ");
            double nota = scanner.nextDouble();
            somaNotas += nota;
            contador++;
        }

        if (numeroAlunos > 0) {
            double media = somaNotas / numeroAlunos;
            System.out.println("A média da turma é: " + media);
        } else {
            System.out.println("Não é possível calcular a média, pois o número de alunos é zero.");
        }

        scanner.close();
    }
}

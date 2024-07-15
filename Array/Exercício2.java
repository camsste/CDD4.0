package Array;
import java.util.Scanner;

public class Exercício2 {

    public static void main(String[] args) {
        int alunos[] = new int[5];
        int soma = 0;
        Scanner input = new Scanner(System.in);

        // Input phase
        for (int x = 0; x < alunos.length; x++) {
            System.out.println("Digite a nota do aluno " + (x + 1) + ":");
            alunos[x] = input.nextInt();
            soma += alunos[x]; // Soma das notas enquanto lê
        }

        // Calculating average
        int media = soma / alunos.length;

        System.out.println("A média das notas dos alunos é: " + media);

        // Fechando o Scanner após o uso
        input.close();
    }
}

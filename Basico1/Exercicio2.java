package Basico1;

import java.util.Scanner;

public class Exercicio2 {
    public static void main(String[] args) {
        int num;
        Scanner input = new Scanner(System.in);
        
        System.out.print("Digite um número inteiro: ");
        num = input.nextInt();
        
        if(num > 0) {
            System.out.println("É positivo");
        } else if(num < 0) {
            System.out.println("É negativo");
        } else {
            System.out.println("É zero");
        }
        
        input.close(); // Fechar o Scanner após o uso
    }
}
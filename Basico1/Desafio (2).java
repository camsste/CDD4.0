package Basico1;

import java.util.Scanner;

public class Desafio {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Perguntas
        System.out.println("Responda com 'sim' ou 'não' para as seguintes perguntas:");
        System.out.print("Telefonou para a vítima? ");
        String resposta1 = scanner.nextLine().trim().toLowerCase();
        System.out.print("Esteve no local do crime? ");
        String resposta2 = scanner.nextLine().trim().toLowerCase();
        System.out.print("Mora perto da vítima? ");
        String resposta3 = scanner.nextLine().trim().toLowerCase();
        System.out.print("Devia para a vítima? ");
        String resposta4 = scanner.nextLine().trim().toLowerCase();
        System.out.print("Já trabalhou com a vítima? ");
        String resposta5 = scanner.nextLine().trim().toLowerCase();

        // Contagem de respostas positivas
        int contagemSim = 0;
        if (resposta1.equals("sim")) contagemSim++;
        if (resposta2.equals("sim")) contagemSim++;
        if (resposta3.equals("sim")) contagemSim++;
        if (resposta4.equals("sim")) contagemSim++;
        if (resposta5.equals("sim")) contagemSim++;

        // Classificação
        System.out.print("\nClassificação: ");
        if (contagemSim == 2) {
            System.out.println("Suspeita");
        } else if (contagemSim == 3 || contagemSim == 4) {
            System.out.println("Cúmplice");
        } else if (contagemSim == 5) {
            System.out.println("Assassino");
        } else {
            System.out.println("Inocente");
        }

        scanner.close();
    }
}

package basico3;
import java.util.Scanner;
import java.util.StringTokenizer;

public class exercicio15 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.println("Digite uma frase especial: ");
		String Pergunta = input.nextLine(); // Lê a frase do usuário
		
		StringTokenizer exemplo = new StringTokenizer(Pergunta);
		System.out.println("Número de palavras na frase: " + exemplo.countTokens());
		
		input.close(); // Fechar o Scanner após o uso é uma boa prática
	}

}

package repeticoes;

public class Exercicio3 {

    public static void main(String[] args) {
        System.out.println("Números pares de 1 a 100:");

        int i = 1;
        while (i <= 100) {
            if (i % 2 == 0) {
                System.out.print(i + " ");
            }
            i++;
        }
    }
}

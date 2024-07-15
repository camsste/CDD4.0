package basico3;

public class exercicio18 {

    public static void main(String[] args) {
        
        String caracteres[] = {"a", "vida", "é", "bela"};
        
        for(int x = 0; x < 4; x++) {
            // Converte cada palavra para maiúsculas e imprime
            System.out.print(caracteres[x].toUpperCase() + " ");
        }
    }

}

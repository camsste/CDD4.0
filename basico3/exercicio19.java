package basico3;

public class exercicio19 {

    public static void main(String[] args) {
        
        String caracteres[] = {"a", "vida", "é", "bela"};
        
        // Inverte a ordem do array
        for(int i = caracteres.length - 1; i >= 0; i--) {
            // Converte cada palavra para maiúsculas e imprime
            System.out.print(caracteres[i].toUpperCase() + " ");
        }
    }

}

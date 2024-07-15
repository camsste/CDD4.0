package obj;

public class ClassePessoa {
    String nome;
    String acao = " "; 

    public void andar() {
        if (acao.equals(" ")) {
            acao = "andando";
            System.out.println(nome + " começou a andar.");
        } else if (acao.equals("andando")) {
            System.out.println(nome + " já está andando.");
        } else if (acao.equals("dormindo")) {
            System.out.println(nome + " não pode andar pois já está dormindo.");
        } else if (acao.equals("comendo")) {
            System.out.println(nome + " não pode andar porque está comendo.");
        }
    	}

    public void comer() {
        if (acao.equals(" ")) {
            acao = "comendo";
            System.out.println(nome + " começou a comer.");
        } else if (acao.equals("andando")) {
            System.out.println(nome + " não pode comer pois está andando.");
        } else if (acao.equals("dormindo")) {
            System.out.println(nome + " não pode comer pois está dormindo.");
        } else if (acao.equals("comendo")) {
            System.out.println(nome + " já está comendo.");
        }
    	}

    public void dormir() {
        if (acao.equals(" ")) {
            acao = "dormindo";
            System.out.println(nome + " começou a dormir.");
        } else if (acao.equals("andando")) {
            System.out.println(nome + " não pode dormir pois está andando.");
        } else if (acao.equals("dormindo")) {
            System.out.println(nome + " já está dormindo.");
        } else if (acao.equals("comendo")) {
            System.out.println(nome + " não pode dormir pois está comendo.");
        }
    	}
    public void pararAndar() {
    	if(acao.equals("andando")) {
    	acao = " ";
    	System.out.println("ele parou de andar");
    	}
    	}
    public void pararComer() {
    	if(acao.equals("comendo")) {
    		acao = " ";
    		System.out.println("ele parou de comer");
    	}
    	}
    public void pararDormir() {
    	if(acao.equals("dormindo")) {
    		acao = " ";
    		System.out.println("ele parou de dormir");
    	}
    	}
    	}
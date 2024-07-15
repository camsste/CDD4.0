package basico3;

public class exercicio9 {
	
	public static void main(String[] args) {
	    String s1 = "Hello";
	    String s2 = "HELLO";
	    
	    boolean b1 = s1.equals("Hello");
	    boolean b2 = s1.equals(s2);
	    boolean b3 = s1.equalsIgnoreCase(s2);
	    boolean b4 = s1.equalsIgnoreCase("azul");
	    
	    System.out.println(b1);
	    System.out.println(b2);
	    System.out.println(b3);
	    System.out.println(b4);

 }
}

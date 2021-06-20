import java.util.Scanner;


public class WarmupRev {
  
	public static String cold(String t) {
		return t.substring(17) + t.substring(0, 17);
	}

	public static String rcold(String t) {
		return t.substring(16) + t.substring(0, 16);
	}
	
	public static String cool(String t) {
		String s = "";
		for (int i = 0; i < t.length(); i++)
			if (i % 2 == 0)
				s += (char) (t.charAt(i) + 3 * (i / 2));
			else
				s += t.charAt(i);
		return s;
	}

	public static String rcool(String t) {
		String s = "";
		for (int i = 0; i < t.length(); i++)
			if (i % 2 == 0)
				s += (char) (t.charAt(i) - 3 * (i / 2));
			else
				s += t.charAt(i);
		return s;
	}
		
	public static String warm(String t) {
		String a = t.substring(0, t.indexOf("l") + 1);
		String t1 = t.substring(t.indexOf("l") + 1);
		String b = t1.substring(0, t1.indexOf("l") + 1);
		String c = t1.substring(t1.indexOf("l") + 1);
		return c + b + a;
	}


	
	public static String hot(String t) {
		int[] adj = {-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 
				21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, 
				-73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13};
		String s = "";
		for (int i = 0; i < t.length(); i++)
			s += (char) (t.charAt(i) + adj[i]);
		return s;
	}

	public static String rhot(String t) {
		int[] adj = {-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 
				21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, 
				-73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13};
		String s = "";
		for (int i = 0; i < t.length(); i++)
			s += (char) (t.charAt(i) - adj[i]);
		return s;
	}

	public static String rwarm(String test, int i) {
                String a1 = test.substring(test.indexOf("l") + 1);                
                String cb1 = test.substring(0,test.indexOf("l") + 1);            
                String c1 = cb1.substring(0,i); 
                String b1 = cb1.substring(i);
                return a1+b1+c1;


        }

	public static void main(String[] args) {
		String match = "4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy";
                String flag = "";
                for (int i = 0; i < 27; i++) {                       
                       String flag1 = rcold(rcool(rwarm(rhot(match),i)));
                       System.out.println(i + "    =>  " + flag1);
                       if (flag1.length() == 33 && hot(warm(cool(cold(flag1)))).equals(match)) {
			           if (flag1.substring(0,5).equals("flag{")) {
                                       flag = flag1;
                                   }
                       }
                }
                System.out.println();
                System.out.println("The flag is " + flag); // flag{1ncr34s3_1n_3nth4lpy_0f_5y5} with i = 15
                

	}
  
}

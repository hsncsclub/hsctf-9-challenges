import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Stack;

public class ATCSSolveScript {
	
	public static String stackAttack(String in) {
		Stack<Character> s = new Stack<>();
		for (char c: in.toCharArray())
			s.push(c);
		String res = "";
		int i = 0;
		while (!s.isEmpty()) {
			res += (char)(s.pop() - i);
			i = (i + 1) % 4;
		}
		return res;
	}

	public static String recurses(String in, String out, int i) {
		if (in.isEmpty())
			return out;
		String res = out;
		if (i == 0)
			res += in.charAt(i);
		else
			res = in.charAt(i) + res;
		if (i == 0)
			return recurses(in.substring(1), res, 1);
		return recurses(in.charAt(0) + in.substring(2), res, 0);
	}

	public static String linkDemLists(String in) {
		LinkedList<Character> lin = new LinkedList<>();
		for (char x: in.toCharArray())
			lin.add(x);
		String res = "";
		ListIterator<Character> iter = lin.listIterator(in.length()/2);
		while (iter.hasNext())
			res += iter.next();
		iter = lin.listIterator(in.length()/2);
		while (iter.hasPrevious())
			res += iter.previous();
		return res;
	}
	
	public static String antiLink(String in) {
		String res = "";
		for (int i = in.length()/ 2 - 1; i >= 0; i --)
			res += in.substring(in.length()/2).toCharArray()[i];
		res += in.substring(0, in.length()/2);
		return res;
	}
	
	public static String antiRecur(String in) {
		char[] arr = new char[in.length()];
		int j = 0;
		for (int i = in.length() - 1; i >= 0; i -= 2) {
			arr[i] = in.charAt(j);
			j++;
		}
		for (int i = 0; i < in.length(); i += 2) {
			arr[i] = in.charAt(j);
			j++;
		}
		return new String(arr);
	}
	
	public static String antiStack(String in) {
		String res = "";
		for (int i = in.length() - 1; i >= 0; i--) {
			res += (char)(in.charAt(i) + (i % 4));
		}
		return res;
	}
	
	public static void main(String[] args) {
		String flag = antiStack(antiRecur(antiLink("20_a1qti0]n/5f642kb\\2`qq4\\0q")));
		System.out.println("flag{" + flag + "}");	
	}

}

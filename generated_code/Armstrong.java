public class Main { public static void main(String[] args) {
	int num = 153;
	int sum = 0;
	for(int i = 0; i <= String.valueOf(num).length(); i++){
		sum += Math.pow(Integer.parseInt(String.valueOf(num).substring(i, i+1)), 3);
	}
	if(sum == num) System.out.println("Armstrong Number"); else System.out.println("Not an Armstrong Number");
} }
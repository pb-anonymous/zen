public class Average {
public static void main(String[] args) {
int sum = 0;
int count = 0;
for (int i = 1; i <= 10; i++) {
sum += i;
count++;
}
int average = sum / count;
System.out.println("The average is " + average);
}
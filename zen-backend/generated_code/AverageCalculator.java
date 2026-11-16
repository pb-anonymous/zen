public class AverageCalculator {
public static void main(String[] args) {
int sum = 0;
int count = 0;
for (String student : args) {
sum += Integer.parseInt(student);
count++;
}
System.out.println("The average is " + sum / count);
}
}
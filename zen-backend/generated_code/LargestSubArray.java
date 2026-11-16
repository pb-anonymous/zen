import java.util.ArrayList;
import java.util.List;
public class LargestSubArray {

public static int largestSubArray(int[] arr) {
  List<Integer> list = new ArrayList<>();
  for (int i = 0; i < arr.length; i++) {
    list.add(arr[i]);
  }
  int maxSum = 0;
  int currentSum = 0;
  for (int i = 0; i < list.size(); i++) {
    if (currentSum < 0) {
      currentSum = list.get(i);
    } else {
      currentSum += list.get(i);
    }
    if (currentSum > maxSum) {
      maxSum = currentSum;
    }
  }
  return maxSum;
}

public static void main(String[] args) {
  int[] arr = {17982};
  System.out.println("Largest Sub Array: " + largestSubArray(arr));
}
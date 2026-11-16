public class Palindrome {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    String str = scanner.nextLine();
    boolean isPalindrom = true;
    for(int i=0; i<str.length()/2;i++){
      if(str.charAt(i)!=str.charAt(str.length()-1-i)) {
        isPalindrom=false;
        break;
      }
    }
    if(isPalindrom) {
      System.out.println("The given string is a palindrome");
    } else {
      System.out.println("The given string is not a palindrome");
    }
  }
}
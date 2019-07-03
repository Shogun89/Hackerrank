import java.io.*;
import java.util.*;

public class Solution {


    public static void main(String[] args) {


        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        System.out.println(A.length() + B.length());
        System.out.println(B.compareTo(A) < 0?"Yes":"No");
        String upper = A.substring(0, 1).toUpperCase()+A.substring(1, A.length())+" "+B.substring(0, 1).toUpperCase()+B.substring(1, B.length());
        System.out.println(upper);
        
    }
}




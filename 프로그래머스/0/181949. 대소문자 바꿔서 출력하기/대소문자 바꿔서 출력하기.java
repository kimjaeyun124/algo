// **

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        StringBuilder result = new StringBuilder(); // 대소문자 전환 할 것 저장, StringBuilder로 만들 수 있음
        for (char c : a.toCharArray()) {    // c에 toCharArray로 a를 문자 배열로 만듬
            if (Character.isUpperCase(c)) { // Character.isUpperCase()로 대문자인지 구분
                result.append(Character.toLowerCase(c)); // result에 대문자로 바꾼후 저장, Character.toLowerCase()로 소문자로 변환
            }   else{
                result.append(Character.toUpperCase(c)); // result에 소문자로 바꾼후 저장, Character.toUpperCase()로 대문자로 변환
            }
        }
        System.out.println(result.toString()); // result.toString()으로 문자열로 출력
    }
}
package study;

import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        Arrays.sort(citations);
        
        for(int i = 0; i<citations[citations.length -1]; i++){
            for(int j = 0; j <citations.length; j++){
                if(citations[j] >= i && citations.length - j >= i){
                    answer = i;
                }
            }
        }
        
        return answer;
    }
}

/* 천재의 풀이
 import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);

        int max = 0;
        for(int i = citations.length-1; i > -1; i--){
            int min = (int)Math.min(citations[i], citations.length - i);
            if(max < min) max = min;
        }

        return max;
    }
}
*/

package study;

import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0; //걸린 시간
        
        Queue<Integer> queue = new LinkedList<>();
        
        for(int i = 0; i<bridge_length; i++){
            queue.add(0);
        }
        
        int present = 0; // 현재 다리위에 올라간 무게
        int i = 0;
        int j = 0;
        while(true){
            answer++;
            if(queue.peek() != 0){
                j++;
                if(j==truck_weights.length){
                    break;
                }
            }
            present = present - queue.poll();
            if(i<truck_weights.length && present + truck_weights[i]<= weight){
                present = present + truck_weights[i];
                queue.add(truck_weights[i]);
                i++;
            }
            else{
                queue.add(0);
            }
           
            
        }
        
        
        return answer;
    }
}

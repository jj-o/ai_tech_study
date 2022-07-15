import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for(int i = 0; i<scoville.length; i++){
            pq.add(scoville[i]);
        }
        
        while(true){
            if(pq.peek() >= K){
                return answer;
            }else if(pq.size() == 1){
                return -1;
            }
            
            pq.add(pq.poll() + pq.poll()*2);
            answer += 1;
        }
    }
}
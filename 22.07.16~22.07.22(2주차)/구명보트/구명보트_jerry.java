package study;

import java.util.*;

class Solution {
            public int solution(int[] people, int limit) {
        	int answer = 0;
        
        	ArrayList<Integer> person = new ArrayList<>();
   		    for(int i = 0; i<people.length; i++){
	            person.add(people[i]);
   		    }
	        Collections.sort(person);
        
        	while(!person.isEmpty()){
            	answer++;
            	int i = person.remove(0);
            	for(int p = person.size()-1; p>=0; p--){
                	if(i+person.get(p)<=limit){
                    	person.remove(p);
                    	break;
                	}
            	}
        	}
        	return answer;
    	}
}

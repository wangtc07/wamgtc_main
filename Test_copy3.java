package _0T;

import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class Test {
	public static void main(String[] args) {
		Queue pq = new LinkedList();
		
		for (int i = 1; i < 6; i++) {
			pq.add(i);
        }
        
        for (int i = 1; i < 6; i++) {
        	System.out.println(pq.offer(i));
        }
		
		pq.offer(1);
//		pq.add(500);
//		pq.add(400);
		pq.offer(4);

		System.out.println(pq);
	}
	
}

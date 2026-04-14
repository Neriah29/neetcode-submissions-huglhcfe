class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        prioritize by frequency 
        have a queue of the format([no_remaining, time_to_get_back])
        have maxHeap
        increment time variable 
        """
        time = 0
        queue = deque([])
        count = Counter(tasks)
        maxHeap = [-num for num in count.values()]
        heapq.heapify(maxHeap)

        while queue or maxHeap:
            #we are going to change the time for each operation.
            #pop the most frequent
            #update its frequency and cooldown, append to the queue
            #check if first element in the queue can come back 
            time += 1
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                if freq < -1:
                    queue.append((freq+1, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
                
        return time
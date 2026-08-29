class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting_temparatures = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if waiting_temparatures:
                top = waiting_temparatures[-1]
                while waiting_temparatures and temperatures[i] > temperatures[top]:
                    
                    waiting_temparatures.pop()
                    result[top] = i - top
                    if waiting_temparatures:
                        top = waiting_temparatures[-1]
            waiting_temparatures.append(i)

        return result
        
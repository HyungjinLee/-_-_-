import heapq
def solution(scoville, K):
    scoville.sort() 
    heapq.heapify(scoville)
    answer=0
    while scoville and scoville[0] < K:
        if len(scoville) == 1 : # 마지막 하나 남은 경우
            return -1
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        heapq.heappush(scoville,f+2*s)
        answer+=1
    return answer
        
    
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(scoville[0] < K) and (len(scoville) > 1):
        heapq.heappush(scoville, (heapq.heappop(scoville) + heapq.heappop(scoville)*2))
        answer = answer + 1
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    else:
        return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 10000
solution(scoville, K)

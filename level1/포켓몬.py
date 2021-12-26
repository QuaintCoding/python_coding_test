def solution(nums):
    take = []
    answer = 0
    for i in nums:
        if i not in take:
            take.append(i)
    if(len(take) > (len(nums)/2)):
        answer = int(len(nums)/2)
    else:
        answer = len(take)
    return answer

nums = [3,3,3,2,2,4]
solution(nums)



# def solution(nums):
#     answer = 0
#     myList = set(nums)
#     if len(nums)/2 > len(myList):
#         answer = len(myList)
#     else:
#         answer = len(nums)/2
#     return answer
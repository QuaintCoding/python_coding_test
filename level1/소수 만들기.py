def solution(nums):
    answer = 0

    print('Hello Python')
    one_pick = -1
    two_pick = -1
    three_pick = -1
    printp = 1;
    sum = 0;
    flag = -1;
    for i in range(len(nums)-2):
        one_pick = nums[i]
        for j in range(i+1, len(nums)-1):
            two_pick = nums[j]
            for k in range(j+1, len(nums)):
                flag = -1
                three_pick = nums[k]
                print(str(one_pick) + " " + str(two_pick) + " " + str(three_pick))
                sum = one_pick+two_pick+three_pick
                for t in range(2, int(sum/2)):
                    if (sum % t) == 0:
                        flag = 1
                if(flag != 1):
                    answer = answer + 1



    return answer
n =[1,2,7,6,4]
answer = solution(n)
print(answer)
def solution(record):
    answer = []
    tempStr = "";
    dict = {}
    for s in record:
        array = s.split(" ")
        if array[0] == "Enter" or array[0] == "Change":
            dict[array[1]] = array[2]
    for s in record:
        array = s.split(" ")
        if array[0] == "Enter":
            tempStr = dict[array[1]] + "님이 들어왔습니다."
            answer.append(tempStr)
        elif array[0] == "Leave":
            tempStr = dict[array[1]] + "님이 나갔습니다."
            answer.append(tempStr)
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)

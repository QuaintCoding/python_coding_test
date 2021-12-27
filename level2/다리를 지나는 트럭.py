# https://this-programmer.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Level2%ED%8C%8C%EC%9D%B4%EC%8D%AC3python3-%EB%8B%A4%EB%A6%AC%EB%A5%BC-%EC%A7%80%EB%82%98%EB%8A%94-%ED%8A%B8%EB%9F%AD
def solution(bridge_length, weight, truck_weights):
    count = 0
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        count += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    print(count)

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
solution(bridge_length, weight, truck_weights)
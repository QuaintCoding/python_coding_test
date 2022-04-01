def dfs(n, computers, visited):
    if not visited[n]:
        visited[n] = True
        for i in range(len(computers)):
            if i != n and computers[n][i] == 1:
                visited = dfs(i, computers, visited)
    return visited


def solution(n, computers):
    answer = 0
    count = 0
    visited = [False for i in range(n)]

    while not all(visited):
        visited = dfs(visited.index(False), computers, visited)
        answer += 1
    print(answer)
    return answer

    # def solution(n, computers):
    # answer = 0
    # visited = [False for i in range(n)]
    # for com in range(n):
    #     if visited[com] == False:
    #         BFS(n, computers, com, visited)
    #         answer += 1
    # return answer

# def BFS(n, computers, com, visited):
#     visited[com] = True
#     queue = []
#     queue.append(com)
#     while len(queue) != 0:
#         com = queue.pop(0)
#         visited[com] = True
#         for connect in range(n):
#             if connect != com and computers[com][connect] == 1:
#                 if visited[connect] == False:
#                     queue.append(connect)
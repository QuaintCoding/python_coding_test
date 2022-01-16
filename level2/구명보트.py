def solution(people, limit):
    boat = 0
    people.sort()
    i = 0
    j = len(people) - 1
    while i <= j:
        boat += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return boat

people = [70, 50, 80, 50, 90]
limit = 100

solution(people, limit)
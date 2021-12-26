def solution(phone_book):
    phone_book.sort()
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    return True


phone_book = ["119", "97674223", "1195524421", "1191", "976742231", "11955244211"]
solution(phone_book)


def solution(phone_book):
    answer = True
    hash_map = {}

    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
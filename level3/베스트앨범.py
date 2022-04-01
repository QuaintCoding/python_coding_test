def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    print(d)
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    print("d", d)
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    print("genreSort", genreSort)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        print("d[g]", d[g], d[g][0], d[g][-1])
        print("temp", temp)
        answer += temp[:min(len(temp),2)]

    print(answer)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

solution(genres, plays)


def solution(genres, plays):
    answer = []
    genres_dict_count = {}
    # key는 genres, value는 count로 장르별로 구분하기
    for i in range(len(genres)):
        if genres[i] in genres_dict_count:
            genres_dict_count[genres[i]].append(plays[i])
        else:
            genres_dict_count[genres[i]] = []
            genres_dict_count[genres[i]].append(plays[i])
    # print(genres_dict_count)

    # dict에서 key에 대한 value sum으로 정렬하기 item[1]이 value 배열
    sorted_dict = dict(sorted(genres_dict_count.items(), key=lambda item: sum(item[1]), reverse=True))
    # print(sorted_dict)
    # sorted_dict에서 value sort하기
    for key, value in sorted_dict.items():
        value.sort(reverse=True)
        count = 0
        # sort하면 순서대로 v를 plays 배열에서 index 찾아서 answer에 append(2개씩만)
        for v in value:
            if count == 2:
                break
            index = plays.index(v)
            plays[index] = -1
            answer.append(index)
            count += 1
    return answer
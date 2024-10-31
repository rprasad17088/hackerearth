def fav_singers(singers):
    singer_count = {}
    for singer in singers:
        if singer in singer_count:
            singer_count[singer] += 1
        else:
            singer_count[singer] = 1
    max_singer_count = max(singer_count.values())
    num_fav_singers = 0
    for count in singer_count.values():
        if count == max_singer_count:
            num_fav_singers += 1
    return num_fav_singers

n = int(input())
singers = list(map(int,input().split()))

if len(singers) != n:
    print("Number of input songs not equal to playlist songs")

print(fav_singers(singers))

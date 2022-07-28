
def solution(genres, plays):
    
    album = {}
    sum_l = {}
    
    for i in range(len(genres)):
        if genres[i] not in album:
            album[genres[i]] = [(plays[i], i)]
            sum_l[genres[i]] = plays[i]
        else:
            album[genres[i]].append( (plays[i], i))
            sum_l[genres[i]] += plays[i]
            
    sort_sum = sorted(sum_l.items(), key= lambda x : x[1], reverse=True)
    # print('sort_sum = ', sort_sum)
    
    for key in album.keys():
        album[key].sort(key = lambda x : x[0], reverse=True)
    # print('album = ', album)
    
    result_dic = {}
    for i in sort_sum:
        for key in album.keys():
            if i[0] == key:
                result_dic[key] = album[key]
    # print('result_dic = ', result_dic)
    result = []
    for value in result_dic.values():
        if len(value) > 1:
            for i in range(2):
                result.append(value[i][1])
        else:
            result.append(value[0][1])
    
    return result
                
            
    
    
    
                
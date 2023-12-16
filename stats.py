from typing import List

name_k = 'name'
min_k = 'min'
max_k = 'max'
mean_k = 'mean'

def get_stats(data: List[float], name: str):
    data.sort()
    min_ = data[0]
    max_ = data[len(data) - 1]
    mean = data[len(data) // 2]
    stats = {
        name_k: name,
        min_k: min_,
        max_k: max_,
        mean_k: mean
    }
    return stats

def print_stats(stats: List):
    print(
        '''name     min      max     mean\n'''
    )
    for i in range(len(stats)):
        print(
            f'''{stats[i][name_k]}      {stats[i][min_k]}       {stats[i][max_k]}       {stats[i][mean_k]}\n'''
        )
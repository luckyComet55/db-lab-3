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
    print(f'list len: {len(stats)}\n')
    print(
        '''name     min      max     mean\n'''
    )
    for stat in stats:
        print(
            f'''{stat[name_k]}      {stat[min_k]}       {stat[max_k]}       {stat[mean_k]}\n'''
        )
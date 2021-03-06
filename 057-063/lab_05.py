import statistics


def mean(lst):
    return sum(lst) / len(lst)


def median(lst):
    sorted_list = sorted(lst)
    list_len = len(sorted_list)
    med_idx = list_len // 2
    if list_len % 2 == 1:
        return sorted_list[med_idx]
    else:
        return sum(sorted_list[med_idx - 1:med_idx + 1]) / 2


def count_unique(lst):
    return len(set(lst))


if __name__ == '__main__':
    with open("lab_05.txt", "r") as f:
        temperatures = list(map(float, f.readlines()))
    print("max:", max(temperatures))
    print("min:", min(temperatures))
    print("count_unique:", count_unique(temperatures))
    print("mean:", mean(temperatures))
    print("median:", median(temperatures))
    print("statistics.mean:", statistics.mean(temperatures))
    print("statistics.median:", statistics.median(temperatures))

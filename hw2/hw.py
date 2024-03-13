from sorter import radix_sort


def get_input():
    try:
        return input()
    except EOFError:
        return ''


if __name__ == "__main__":

    inp = get_input()
    data = []
    while inp:
        data.append(inp.split('\t'))
        inp = get_input()
    indexes = list(range(len(data)))

    def key_func(el, index):
        if len(data[el][0]) < index:
            return data[el][0][index]
        return None

    def len_func(el):
        return len(data[el][0])

    sorted_indexes = radix_sort(indexes, len_func=len_func, key_func=key_func)

    for idx in sorted_indexes:
        print(data[idx][0] + "\t" + data[idx][1])

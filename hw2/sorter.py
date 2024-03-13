from typing import List, Any, Callable
from functools import partial


def default_key(el, index):
    if index < len(el):
        return el[index]
    return None


def _radix_sort_bucket(bucket: List[Any], index: int, key_func: Callable):
    not_end_bucket = []
    buckets = []
    bucket_index = -1
    for el in bucket:
        if key_func(el, index) is None:
            if len(buckets) == 0:
                bucket_index += 1
                buckets.append([])
            buckets[bucket_index].append(el)
        else:
            not_end_bucket.append(el)

    if len(not_end_bucket) == 0:
        return True, buckets

    flatten_sorted = sorted(not_end_bucket, key=partial(key_func, index=index))
    last_key = None
    for el in flatten_sorted:
        key = key_func(el, index=index)
        if key != last_key:
            bucket_index += 1
            buckets.append([])
        buckets[bucket_index].append(el)
        last_key = key

    return False, buckets


def radix_sort(seq: List[Any],
               len_func: Callable = len,
               key_func: Callable = default_key
               ) -> List[int]:
    _, buckets = _radix_sort_bucket(seq, -1, lambda x, index: len_func(x))

    index_to_sort = 0
    while True:
        end = True
        new_buckets = []
        for bucket in buckets:
            is_end, new_bucket = _radix_sort_bucket(bucket,
                                                    index_to_sort,
                                                    key_func)
            end &= is_end
            new_buckets += new_bucket
        buckets = new_buckets
        index_to_sort += 1
        if end:
            break

    return [el for bucket in buckets for el in bucket]

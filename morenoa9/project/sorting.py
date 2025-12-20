def quick_sort(songs, key):
    if len(songs) <= 1:
        return songs

    pivot = songs[len(songs) // 2]
    left = [s for s in songs if getattr(s, key) < getattr(pivot, key)]
    middle = [s for s in songs if getattr(s, key) == getattr(pivot, key)]
    right = [s for s in songs if getattr(s, key) > getattr(pivot, key)]

    return quick_sort(left, key) + middle + quick_sort(right, key)


def merge_sort(songs, key):
    if len(songs) <= 1:
        return songs

    mid = len(songs) // 2
    left = merge_sort(songs[:mid], key)
    right = merge_sort(songs[mid:], key)

    return merge(left, right, key)


def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if getattr(left[i], key) <= getattr(right[j], key):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

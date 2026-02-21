def reverse_list(items):
    n = len(items)
    for i in range(n // 2):  # Only go to middle
        j = n - 1 - i
        items[i], items[j] = items[j], items[i]

    # 5. Verify
    return items

def reverse_parts(s, k):
    result = ""
    i = 0

    while i < len(s):
        part = s[i:i + 2 * k]
        first_k = part[:k]
        rest = part[k:]
        reversed_first_k = first_k[::-1]
        result += reversed_first_k + rest
        i += 2 * k

    return result

print(reverse_parts("qwertyu", 2))
print(reverse_parts("tyui", 2))
print(reverse_parts("asdlkjhgfdd", 3))
print(reverse_parts("р", 2))


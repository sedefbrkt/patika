def reverse_nested(lst):
    reversed_list = []
    for item in reversed(lst):
        if isinstance(item, list):
            reversed_list.append(reverse_nested(item))
        else:
            reversed_list.append(item)
    return reversed_list

# Örnek kullanım
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_nested(input_list)
print(output_list)  # Çıktı: [[[7, 6, 5], [4, 3], [2, 1]]]

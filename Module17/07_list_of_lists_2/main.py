nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

very_nice_list = [number for a_list in nice_list for b_list in a_list for number in b_list]
print(very_nice_list)
def my_zip(first_object, second_object):
    if not (isinstance(first_object, dict) and isinstance(second_object, dict)):
        zipper = ((i_first_object_item, j_second_object_item)
                  for i_first_object_index, i_first_object_item in enumerate(first_object)
                  for j_second_object_index, j_second_object_item in enumerate(second_object)
                  if i_first_object_index == j_second_object_index)
    elif isinstance(first_object, dict) and not isinstance(second_object, dict):
        zipper = ((i_first_object_item, j_second_object_item)
                  for i_first_object_index, i_first_object_item in first_object.items()
                  for j_second_object_index, j_second_object_item in enumerate(second_object)
                  if i_first_object_index == j_second_object_index)
    elif not isinstance(first_object, dict) and isinstance(second_object, dict):
        zipper = ((i_first_object_item, j_second_object_item)
                  for i_first_object_index, i_first_object_item in enumerate(first_object)
                  for j_second_object_index, j_second_object_item in second_object.items()
                  if i_first_object_index == j_second_object_index)
    elif isinstance(first_object, dict) and isinstance(second_object, dict):
        zipper = ((i_first_object_item, j_second_object_item)
                  for i_first_object_index, i_first_object_item in first_object.items()
                  for j_second_object_index, j_second_object_item in second_object.items()
                  if i_first_object_index == j_second_object_index)
    return zipper


my_str = 'abcd'
my_tuple = (10, 20, 30, 40)

zipper = my_zip(my_str, my_tuple)
print(zipper)
for i_twin in zipper:
    print(i_twin)

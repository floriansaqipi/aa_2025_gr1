def can_form_array(target_array, pieces_list):
    first_num_to_piece = {piece[0]: piece for piece in pieces_list}

    current_index = 0
    total_length = len(target_array)

    while current_index < total_length:
        current_number = target_array[current_index]
        if current_number not in first_num_to_piece:
            return False

        current_piece = first_num_to_piece[current_number]
        for number in current_piece:
            if target_array[current_index] != number:
                return False
            current_index += 1

    return True


arr1 = [91, 4, 64, 78]
pieces1 = [[78], [4, 64], [91]]
print(can_form_array(arr1, pieces1))

arr2 = [49, 18, 16]
pieces2 = [[16, 18, 49]]
print(can_form_array(arr2, pieces2))

arr3 = [49, 18, 16]
pieces3 = [[49, 18], [16]]
print(can_form_array(arr3, pieces3))

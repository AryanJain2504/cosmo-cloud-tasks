list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    # create a dictionary to store the merged information
    final_dict = {}
    
    # iterate over the first list
    for student_info in list_1:
        # get the student id
        student_id = student_info.get('id')
        
        # create a new dictionary with the student information
        student_dict = {'id': student_id,'name': student_info.get('name'), 'age': student_info.get('age'), 'marks': student_info.get('marks'), 'roll_no': student_info.get('roll_no'), 'extra_info': student_info.get('extra_info')}
        
        # add the student dictionary to the merged dictionary using the student id as key
        final_dict[student_id] = student_dict
    
    # iterate over the second list
    for student_info in list_2:
        # get the student id
        student_id = student_info.get('id')
        
        # check if the student id exists in the merged dictionary
        if student_id in final_dict:
            # update the student dictionary with the new information
            final_dict[student_id].update({'marks': student_info.get('marks'), 'roll_no': student_info.get('roll_no'), 'extra_info': student_info.get('extra_info')})
        else:
            # create a new dictionary with the student information
            student_dict = {'id': student_id,'marks': student_info.get('marks'), 'roll_no': student_info.get('roll_no'), 'extra_info': student_info.get('extra_info')}
            
            # add the student dictionary to the merged dictionary using the student id as key
            final_dict[student_id] = student_dict
    
    # create a list with the merged dictionary values
    merged_list = list(final_dict.values())
    
    return merged_list

list_3 = merge_lists(list_1, list_2)
print('list_3: ',list_3)
sorted_list = sorted(list_3, key=lambda x: x['id'])
print('Final sorted List: ',sorted_list)

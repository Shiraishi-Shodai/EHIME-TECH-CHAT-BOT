# array = [1, 2, 3, 4]
# if array:
#     print(1)
    
# array = [1, 2]
# # 連想配列
# dict = {
#     '1': 'Hello',
#     '2': 'Good Morning',
#     }

# if array:
#     for value in array:
#         print(value)
# if dict:
#     for key in dict:
#         print(f'{key}: {dict[key]}')

dict01 = {'1': 'Hello'}
dict02 = {'2': 'Good Morning'}
array = [dict01, dict02]

if array:
    for dict in array:
        for key in dict:
            print(f'{key} : {dict[key]}')
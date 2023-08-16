# array = [1, 2, 3, 4]
# # arrayが空でなければTrue,空ならFalseを返す
# if array:
#     for i in array:
#         print(i)
# else:
#     print('None')
    
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
#     for key in dict.keys():
#         print(f'{key}: {dict[key]}')

dict01 = {
    '1': 'Hello',
    '2': 'Hello2',
    }
dict02 = {'2': 'Good Morning'}
array = [dict01, dict02]

if array:
    for dict in array:
        for key in dict:
            print(f'{key} : {dict[key]}')
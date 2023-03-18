def flatten_list(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

def get_input():
    input_str = input("Lütfen listenizi girin : ")
    input_list = []
    try:
        input_list = eval(input_str)
    except:
        print("Hata: Geçersiz girdi!")
    return input_list

input_list = get_input()
output_list = flatten_list(input_list)
print(output_list)
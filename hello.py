
# t_in_city = {'city': 'Москва', 'temperature': 24}
# print(t_in_city['city'])
# t_in_city['temperature'] = 24 - 5
# print(t_in_city)
# print(t_in_city.get('country', 'Russia'))
# t_in_city['data'] = "27.05.2019"
# print(len(t_in_city))

def get_sum(one, two, delimeter='&'):
    return (one+delimeter+two).upper()
res_str = get_sum("Learn", "python")
print(res_str)




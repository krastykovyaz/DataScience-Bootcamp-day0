def reverse_dict():
    result_dict = {}
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    mapping = {}
    for i, (country, num) in enumerate(list_of_tuples):
        mapping[num] = mapping.get(num, []) + [i]
        result_dict[(i, num)] = country

    print(*[f'\'{num[1]}\' : \'{country}\'' for num, country in result_dict.items()], sep='\n')


if __name__ == '__main__':
    reverse_dict()

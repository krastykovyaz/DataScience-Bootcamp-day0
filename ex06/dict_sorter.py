def reverse_dict():
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
    list_of_tuples = sorted(list_of_tuples,
                            key=lambda x: int(x[1]), reverse=True)
    dict_of_tuples = dict(list_of_tuples)
    print('\n'.join([row[0] for row in
                     sorted(sorted(dict_of_tuples.items(), key=lambda x: x[0]),
                            key=lambda x: int(x[1]), reverse=True)]))


if __name__ == '__main__':
    reverse_dict()

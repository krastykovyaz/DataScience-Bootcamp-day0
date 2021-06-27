def data_type():
    int_var = 0
    str_var = str(int_var)
    float_var = float(int_var)
    bool_var = bool(int_var)
    list_var = [int_var]
    dict_var = {int_var: int_var}
    tuple_var = (int_var,)
    set_var = {int_var}
    print('[', ', '.join(list(map(
            lambda x: str(type(x)).replace(
                '<class ', '').replace('>', '').replace("'", ''),
            [int_var, str_var, float_var, bool_var, list_var, dict_var,
             tuple_var, set_var]))), ']', sep='')


if __name__ == '__main__':
    data_type()

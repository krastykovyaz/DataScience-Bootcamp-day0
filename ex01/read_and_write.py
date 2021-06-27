def change_csv(file):
    result_data = ''
    with open(file) as f:
        for row in f:
            flag = False
            for obj in row.split(','):
                result_data += obj
                if obj[-1] == '\n':
                    continue
                if obj.count('"') == 1:
                    flag = not flag
                if flag:
                    result_data += ','
                else:
                    result_data += '\t'
            result_data.rstrip('\t')
    return result_data


def save_csv(data, filename):
    with open(filename, 'w') as f:
        f.write(data)


if __name__ == '__main__':
    save_csv(change_csv('./ds.csv'), './ds.tsv')

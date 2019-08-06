import configparser
import re, datetime, os


def get_config(path='change_time.ini'):
    file = os.path.isfile(path)
    if not file:
        with open(path, 'w') as file:
            dir_path = os.path.dirname(__file__)
            file.write('[new_option]\ntime=0\npath= %s\ntype=ass' % os.path.abspath(dir_path))
            print(os.path.abspath(dir_path))
    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_file(config):
    name_file = None
    default_path = config['new_option']['path']
    f_type = '.' + config['new_option']['type']
    if default_path.endswith(f_type):
        full_path = default_path
    else:
        directory_file = os.listdir(default_path)
        for file in directory_file:
            if file.endswith(f_type):
                name_file = file
        if name_file is None:
            raise Exception('Sub File not found.')
        full_path = os.path.join(default_path, name_file)

    return full_path


def get_time(full_path):
    with open(os.path.abspath(full_path), 'rb') as f:
        data = f.read()
        ru_text = data.decode('utf-8')
    if full_path.endswith('ass'):

        list_time = re.findall(r'(\d:\d*:\d*.\d+),', ru_text)
    else:
        list_time = re.findall(r'\d*:\d*:\d*.\d+', ru_text)

    return list_time, ru_text


def change_time(list_time, config, ru_text, full_path):
    for link in list_time:
        link = str(link)
        if full_path.endswith('ass'):
            dot = '.'
            sec_drop = -4
        else:
            dot = ','
            sec_drop = -3
        string_to_time = datetime.datetime.strptime(link, '%H:%M:%S' + dot + '%f')
        plus_time = string_to_time + datetime.timedelta(seconds=int(config['new_option']['time']))
        time_to_string = plus_time.strftime('%H:%M:%S' + dot + '%f')[:sec_drop]
        ru_text = ru_text.replace(link, time_to_string)
    f_type = config['new_option']['type']
    with open(full_path.replace('.' + f_type, 'new.' + f_type), 'wb') as f:
        print(full_path.replace('.' + f_type, 'new.' + f_type))
        print(full_path)
        print('.' + f_type)
        f.write(ru_text.encode('utf-8'))


config = get_config()
full_path = get_file(config)
print(full_path)
list_time, ru_text = get_time(full_path)

change_time(list_time, config, ru_text, full_path)

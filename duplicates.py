import argparse
import os


def are_files_duplicates(file_1, file_2):
    if not (file_1['full_path'] == file_2['full_path']) and \
            (file_1['file_name'] == file_2['file_name']) and \
            (file_1['file_size'] == file_2['file_size']):
        return True
    else:
        return False


def get_all_path_info(path):
    files_info = []
    for root, dirs, files in os.walk(path):
        for file in files:
            files_info.append({
                'full_path': os.path.join(root, file),
                'file_name': file,
                'file_size': os.path.getsize(os.path.join(root, file))})

    return files_info


def print_all_duplicates(duplicates):
    for dublicate in sorted(duplicates, key=lambda dbc: dbc['file_name']):
        message = "Найден дубликат файла {}, путь {}, размер {}"
        print(message.format(dublicate['file_name'], dublicate['full_path'], dublicate['file_size']))


def get_all_dublicates(files_info):
    dublicates = []
    for file_1 in files_info:
        for file_2 in files_info:
            if are_files_duplicates(file_1=file_1, file_2=file_2) \
                    and file_2 not in dublicates:
                dublicates.append(file_2)
    return dublicates


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('-p', '--path', help='Путь к папке для поиска', required=True)
    arguments = args.parse_args()

    if arguments.path:
        dublicated_files = get_all_dublicates(get_all_path_info(arguments.path))
        print_all_duplicates(dublicated_files)

import argparse
import os

def are_files_duplicates(file_path1, file_path_2):
    pass

def get_all_path_info(path):
    files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            files.append({
                'full_path' : os.path.join(root,file) ,
            'file_name' : file})
            print(files)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('-p','--path',help='A Path for searching duplicates',required=True)
    arguments = args.parse_args()

    if arguments.path :
        get_all_path_info(arguments.path)

from aligo import Aligo
import time

def download_all():
    ali = Aligo()
    file = ali.get_file_by_path('512KB.txt')

    local_folder = ''
    if file.type == 'file':
        start_time = time.time()
        ali.download_file(file=file, local_folder=local_folder)
        end_time = time.time() - start_time
        print("512KB file's downloading duration time: ", end_time)
    else:
        ali.download_folder(file.file_id, local_folder=local_folder)

    ali = Aligo()
    file = ali.get_file_by_path('1MB.txt')

    local_folder = ''
    if file.type == 'file':
        start_time = time.time()
        ali.download_file(file=file, local_folder=local_folder)
        end_time = time.time() - start_time
        print("1MB file's downloading duration time: ", end_time)
    else:
        ali.download_folder(file.file_id, local_folder=local_folder)

    ali = Aligo()
    file = ali.get_file_by_path('2MB.txt')

    local_folder = ''
    if file.type == 'file':
        start_time = time.time()
        ali.download_file(file=file, local_folder=local_folder)
        end_time = time.time() - start_time
        print("2MB file's downloading duration time: ", end_time)
    else:
        ali.download_folder(file.file_id, local_folder=local_folder)

    ali = Aligo()
    file = ali.get_file_by_path('10MB.txt')

    local_folder = ''
    if file.type == 'file':
        start_time = time.time()
        ali.download_file(file=file, local_folder=local_folder)
        end_time = time.time() - start_time
        print("10MB file's downloading duration time: ", end_time)
    else:
        ali.download_folder(file.file_id, local_folder=local_folder)

    ali = Aligo()
    file = ali.get_file_by_path('100MB.txt')

    local_folder = ''
    if file.type == 'file':
        start_time = time.time()
        ali.download_file(file=file, local_folder=local_folder)
        end_time = time.time() - start_time
        print("100MB file's downloading duration time: ", end_time)
    else:
        ali.download_folder(file.file_id, local_folder=local_folder)
        
    ali = Aligo()
    file = ali.get_file_by_path('1GB.txt')

    local_folder = ''
    if file.type == 'file':
        start_time = time.time()
        ali.download_file(file=file, local_folder=local_folder)
        end_time = time.time() - start_time
        print("1GB file's downloading duration time: ", end_time)
    else:
        ali.download_folder(file.file_id, local_folder=local_folder)





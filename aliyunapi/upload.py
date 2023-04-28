from aligo import Aligo
import time

def upload_all():
    ali = Aligo()
    start_time = time.time()
    ali.upload_files(['./data/512KB.txt'])
    end_time = time.time() - start_time
    print("512KB file's uploading duration time: ", end_time)

    ali = Aligo()
    start_time = time.time()
    ali.upload_files(['./data/1MB.txt'])
    end_time = time.time() - start_time
    print("1MB file's uploading duration time: ", end_time)

    ali = Aligo()
    start_time = time.time()
    ali.upload_files(['./data/2MB.txt'])
    end_time = time.time() - start_time
    print("2MB file's uploading duration time: ", end_time)

    ali = Aligo()
    start_time = time.time()
    ali.upload_files(['./data/10MB.txt'])
    end_time = time.time() - start_time
    print("10MB file's uploading duration time: ", end_time)

    ali = Aligo()
    start_time = time.time()
    ali.upload_files(['./data/100MB.txt'])
    end_time = time.time() - start_time
    print("100MB file's uploading duration time: ", end_time)
    
    ali = Aligo()
    start_time = time.time()
    ali.upload_files(['./data/1GB.txt'])
    end_time = time.time() - start_time
    print("1GB file's uploading duration time: ", end_time)



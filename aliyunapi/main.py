from aligo import Aligo
from download import download_all
from upload import upload_all

if __name__ == '__main__':
    ali = Aligo()  # a QR code will pop up for scanning and logging in

    user = ali.get_user()
    print(user.user_name, user.nick_name, user.phone)

    ll = ali.get_file_list()
    for file in ll:
        print(file.file_id, file.name, file.type)

upload_all()
download_all()

print("finished")
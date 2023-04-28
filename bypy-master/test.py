from bypy import ByPy


def upload_512KB_file():
	bp = ByPy()
	print("512KB file's uploading duration time: ")
	bp.upload('./data/512KB.txt')



def upload_1MB_file():
	bp = ByPy()
	print("1MB file's uploading duration time: ")
	bp.upload('./data/1MB.txt')


def upload_2MB_file():
	bp = ByPy()
	print("2MB file's uploading duration time: ")
	bp.upload('./data/2MB.txt')


def upload_10MB_file():
	bp = ByPy()
	print("10MB file's uploading duration time: ")
	bp.upload('./data/10MB.txt')


def upload_100MB_file():
	bp = ByPy()
	print("100MB file's uploading duration time: ")
	bp.upload('./data/100MB.txt')


def upload_1GB_file():
	bp = ByPy()
	print("1GB file's uploading duration time: ")
	bp.upload('./data/1GB.txt')

def download_512KB_file():
	bp = ByPy()
	print("512KB file's downloading duration time: ")
	bp.downfile('512KB.txt', './temp')


def download_1MB_file():
	bp = ByPy()
	print("1MB file's downloading duration time: ")
	bp.downfile('1MB.txt', './temp')


def download_2MB_file():
	bp = ByPy()
	print("2MB file's downloading duration time: ")
	bp.downfile('2MB.txt', './temp')


def download_10MB_file():
	bp = ByPy()
	print("10MB file's downloading duration time: ")
	bp.downfile('10MB.txt', './temp')


def download_100MB_file():
	bp = ByPy()
	print("100MB file's downloading duration time: ")
	bp.downfile('100MB.txt', './temp')


def download_1GB_file():
	bp = ByPy()
	print("1GB file's downloading duration time: ")
	bp.downfile('1GB.txt', './temp')


def test_upload():
	upload_512KB_file()
	upload_1MB_file()
	upload_2MB_file()
	upload_10MB_file()
	upload_100MB_file()
	#upload_1GB_file()


def test_download():
	download_512KB_file()
	download_1MB_file()
	download_2MB_file()
	download_10MB_file()
	download_100MB_file()
	#download_1GB_file()

print("===============Start Uploading Test===================")
test_upload()
print("===============Start Downloading Test=================")
test_download()

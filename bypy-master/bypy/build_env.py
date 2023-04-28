import subprocess
import sys


def install(package, version=None):
    if version is not None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "{}=={}".format(package, version)])
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

packages = {
    "Pillow": "9.5.0",
    "aligo": "5.5.28",
    "certifi": "2022.12.7",
    "charset-normalizer": "3.1.0",
    "coloredlogs": "15.0.1",
    "dill": "0.3.6",
    "humanfriendly": "10.0",
    "idna": "3.4",
    "multiprocess": "0.70.14",
    "pypng": "0.20220715.0",
    "qrcode": "7.4.2",
    "qrcode-terminal": "0.8",
    "requests": "2.28.2",
    "requests-toolbelt": "0.10.1",
    "setuptools": "60.2.0",
    "tqdm": "4.65.0",
    "typing-extensions": "4.5.0",
    "urllib3": "1.26.15",
    "wheel": "0.37.1",
}

for package, version in packages.items():
    install(package, version)

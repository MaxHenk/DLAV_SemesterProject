import subprocess

packages = [
    'torch==1.9.1 torchvision==0.10.1 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html',
    '-c omgarcia gcc-6'
]

for package in packages:
    subprocess.run(['pip', 'install', package])

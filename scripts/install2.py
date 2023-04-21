import subprocess

commands = [
    ['pip', 'install', 'torch==1.9.1', 'torchvision==0.10.1', 'torchaudio==0.9.1', '-f', 'https://download.pytorch.org/whl/torch_stable.html'],
    ['pip', 'install', '-c', 'omgarcia', 'gcc-6']
]

for command in commands:
    subprocess.run(command)

import subprocess
import sys
import os

def run_command(command):
    process = subprocess.run(command, capture_output=True, text=True)
    if process.returncode != 0:
        print(f"Erreur lors de l'exécution de la commande : {' '.join(command)}\n{process.stderr}")
        sys.exit(1)
    else:
        print(f"Commande réussie : {' '.join(command)}\n{process.stdout}")

# Créez un environnement virtuel
venv_path = "open-mmlab"
run_command([sys.executable, "-m", "venv", venv_path])

# Activez l'environnement virtuel
venv_bin = os.path.join(venv_path, "bin")
if os.name == "nt":
    activate_script = os.path.join(venv_bin, "activate.bat")
else:
    activate_script = os.path.join(venv_bin, "activate")

# Installez les packages dans l'environnement virtuel
commands = [
    [os.path.join(venv_bin, "pip"), "install", "torch==1.9.1+cu111", "torchvision==0.10.1+cu111", "torchaudio==0.9.1", "-f", "https://download.pytorch.org/whl/torch_stable.html"],
    # Vous devez installer gcc>=5 séparément sur votre système, en utilisant le gestionnaire de paquets de votre système d'exploitation
    [os.path.join(venv_bin, "pip"), "install", "mmcv-full==1.4.0"],
    [os.path.join(venv_bin, "pip"), "install", "mmdet==2.14.0"],
    [os.path.join(venv_bin, "pip"), "install", "mmsegmentation==0.14.1"],
    ["git", "clone", "https://github.com/open-mmlab/mmdetection3d.git"],
    ["bash", "-c", f"source {activate_script} && cd mmdetection3d && git checkout v0.17.1 && pip install -v -e ."],
    [os.path.join(venv_bin, "pip"), "install", "timm"],
    ["git", "clone", "https://github.com/NVlabs/VoxFormer.git"]
]

for command in commands:
    run_command(command)

#Prerequisite : dataset has to be downloaded 

#Symlink the dataset root to ./kitti
ln -s [SemanticKITTI root] ./kitti
#Copy the calibration files to the dataset folder in the kitti file
cp -r data_odometry_calib/sequences kitti/dataset

#create a virtual environment
python3 -m venv [venv_prepdata_root]
source [venv_prepdata_root]/bin/activate

#Install packages
pip install numpy
pip install tqdm
pip install pyyaml
pip install imageio

#Preprocess the data to generate labels at a lower scale
python label/label_preprocess.py --kitti_root=[SemanticKITTI root] --kitti_preprocess_root=[venv_prepdata_root]


#Prerequisite : download file mobilestereonet at https://github.com/NVlabs/VoxFormer/tree/main/preprocess
#Set current directory to the mobilestereonet folder
cd mobilestereonet
#Create virtual environment
conda env create --file mobilenet.yaml # please modify prefix in .yaml
conda activate mobilenet

#Script to predict depth map
./image2depth.sh
#Script to create pseudo point cloud
./depth2lidar.sh

conda activate preprocess
#Script to sweep voxelization
./lidar2voxel.sh


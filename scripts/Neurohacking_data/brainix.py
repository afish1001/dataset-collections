"""
将3d_images中的nii.gz文件转换为灰度图像
"""
import os
import nibabel as nib
from glob import glob
import matplotlib.pyplot as plt


datasets_path = '../../datasets/Neurohacking_data-0.0'
output_folder = './results'

img_nii_list = glob(os.path.join(datasets_path, 'BRAINIX', 'NIfTI', 'BRAINIX_*.nii.gz'))

for nii in img_nii_list:
    nii_ = nib.load(nii)
    images = nii_.get_data()
    count = 0
    save_folder = os.path.join(output_folder, os.path.basename(nii))
    os.makedirs(save_folder, exist_ok=True)
    for i in range(images.shape[2]):
        save_path = os.path.join(save_folder, '{:0>3d}.png'.format(count))
        plt.imsave(save_path, images[:, :, i], cmap='bone')
        count += 1
    print('Done: {}, num of images: {}, num of output: {}'.format(nii, images.shape[2], count))

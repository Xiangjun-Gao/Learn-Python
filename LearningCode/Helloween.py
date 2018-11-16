#!/usr/bin/env python
from PIL import Image
import numpy as np
import os,os.path

#disp = 0.54 * 721 / (1242 * depth)


def rgb2dd(rgbfile1,rgbfile2,depthfile):
	rgb1 = np.array(Image.open(rgbfile1),dtype = int)
	rgb2 = np.array(Image.open(rgbfile2),dtype = int)
	depth_png = np.array(Image.open(depthfile),dtype = int)
	# make sure we have a proper 16bit depth map here.. not 8bit!
	assert(np.max(depth_png)>255)
	depth = depth_png.astype(np.float32)/256
	depth[depth_png==0] = -1

	disp = 0.54 * 721 / (1242 * depth)
	disp[depth < 0] = -1
	rgb2dd = np.zeros((375,1242,8),dtype = np.float32)

	tup1 = rgb1.shape[0]
	tup2 = rgb1.shape[1]
	if tup1 > 375:
		tup1 = 375
	if tup2 > 1242:
		tup2 = 1242

	rgb2dd[0:tup1,0:tup2,0:3] =  rgb1[0:tup1,0:tup2,:]
	rgb2dd[0:tup1,0:tup2,3:6] =  rgb2[0:tup1,0:tup2,:]
	rgb2dd[0:tup1,0:tup2,6] = disp[0:tup1,0:tup2]
	rgb2dd[0:tup1,0:tup2,7] = depth[0:tup1,0:tup2]

	return rgb2dd

def main():
	depth_val_path_pre = '/home/mcislab/gaoxiangjun/xiangjun/kitti_raw/data_depth_velodyne/val'
	depth_train_path_pre = '/home/mcislab/gaoxiangjun/xiangjun/kitti_raw/data_depth_velodyne/train'
	rgb_path_pre = '/home/mcislab/gaoxiangjun/xiangjun/kitti_raw'

	file1 = open('/home/mcislab/gaoxiangjun/xiangjun/depth_annotated_val_dir_list.txt')
	depth_val_dir_list = file1.readlines()
	file1.close()

	file2 = open('/home/mcislab/gaoxiangjun/xiangjun/depth_annotated_train_dir_list.txt')
	depth_train_dir_list = file2.readlines()
	file2.close()

	for i, name in enumerate(depth_val_dir_list):

		depth_val_dir_list[i] = depth_val_dir_list[i].strip()
		print(i,depth_val_dir_list[i])

		depth_dir_path = os.path.join(depth_val_path_pre,depth_val_dir_list[i],'proj_depth/velodyne_raw/image_02')
		rgb1_dir_path = os.path.join(rgb_path_pre,depth_val_dir_list[i],depth_val_dir_list[i][0:10],depth_val_dir_list[i],'image_02/data')
		rgb2_dir_path = os.path.join(rgb_path_pre,depth_val_dir_list[i],depth_val_dir_list[i][0:10],depth_val_dir_list[i],'image_03/data')

		img_files = os.listdir(depth_dir_path)

		for img in img_files:
			depth_img_path = os.path.join(depth_dir_path,img)
			rgb1_img_path = os.path.join(rgb1_dir_path,img)
			rgb2_img_path = os.path.join(rgb2_dir_path,img)
			np.save(os.path.join('/home/mcislab/gaoxiangjun/xiangjun/npy/kitti_raw/val',depth_val_dir_list[i]+'_'+img[:-4]+'.npy'),rgb2dd(rgb1_img_path,rgb2_img_path,depth_img_path)	)

	for i, name in enumerate(depth_train_dir_list):

		depth_train_dir_list[i] = depth_train_dir_list[i].strip()
		print(i,depth_train_dir_list[i])

		depth_dir_path = os.path.join(depth_train_path_pre,depth_train_dir_list[i],'proj_depth/velodyne_raw/image_02')
		rgb1_dir_path = os.path.join(rgb_path_pre,depth_train_dir_list[i],depth_train_dir_list[i][0:10],depth_train_dir_list[i],'image_02/data')
		rgb2_dir_path = os.path.join(rgb_path_pre,depth_train_dir_list[i],depth_train_dir_list[i][0:10],depth_train_dir_list[i],'image_03/data')

		img_files = os.listdir(depth_dir_path)

		for img in img_files:
			depth_img_path = os.path.join(depth_dir_path,img)
			rgb1_img_path = os.path.join(rgb1_dir_path,img)
			rgb2_img_path = os.path.join(rgb2_dir_path,img)
			np.save(os.path.join('/home/mcislab/gaoxiangjun/xiangjun/npy/kitti_raw/train',depth_train_dir_list[i]+'_'+img[:-4]+'.npy'),rgb2dd(rgb1_img_path,rgb2_img_path,depth_img_path)	)


if __name__ == '__main__':
	main()
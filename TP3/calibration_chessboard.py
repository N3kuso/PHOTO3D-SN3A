import numpy as np
import cv2 as cv
import glob
import matplotlib.pyplot as plt


def calibrate_chessboard(image_files):
	print('Image list:')
	for image_file in image_files:
		print('  - '+image_file)
		img = cv.imread(image_file)
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

		plt.figure(image_file)
		plt.imshow(img)
	
	plt.show()


def main():

	# Load images from data folder
	image_files = glob.glob('data/google_pixel_6/chessboard/6x11/*.jpg')

	calibrate_chessboard(image_files)


if __name__ == "__main__":
	main()
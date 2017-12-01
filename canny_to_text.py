import numpy as np
import cv2
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_image', type=str, help='input image path', default='img.jpg')
    parser.add_argument('--out_file', type=str, help='output text file path', default='img.txt')
    parser.add_argument('--minV', type=int, help='minVal Canny', default='100')
    parser.add_argument('--maxV', type=int, help='maxVal Canny', default='200')

    args = parser.parse_args()

    image_name = args.in_image
    text_file_name = args.out_file
    minV = args.minV
    maxV = args.maxV

    img = cv2.imread(image_name,0)
    img = cv2.Canny(img, minV, maxV)
    np.savetxt(text_file_name, fmt='%d', X=img, newline='\n')

if __name__ == "__main__":
    main()

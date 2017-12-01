# img_to_gray_mat

## files:

* img_show.py - скрипт для расшифровки массива 
* img_to_text.py - скрипт для вывода массива чисел


## install:

pip3 install opencv-python

## launch:

* img to text:
python3 img_to_text.py --in_image [file-name-in.xxx] --out_file [file-name-out.xxx]
example: python3 img_to_text.py --in_image img.jpg --out_file img.txt

* text to img :
python3 img_show.py --in_file [file-name-in.xxx]
example: python3 img_show.py --in_file img.txt


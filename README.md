# img_to_gray_mat

## files:

* img_show.py - скрипт для расшифровки массива 
* img_to_text.py - скрипт для вывода массива значений серого на изображении в текст
* canny_to_text.py - скрипт для вывода массива границ Канни изображения в текст

## install:

pip3 install opencv-python

## launch:

### img to text:
python3 img_to_text.py --in_image [file-name-in.xxx] --out_file [file-name-out.xxx]

default:

  * **--in_file** img.jpg
  * **--out_file** img.txt

>python3 img_to_text.py --in_image img.jpg --out_file img.txt

### text to img :

python3 img_show.py --in_file [file-name-in.xxx]

default:
  
  * **--in_file** img.txt

  >python3 img_show.py --in_file img.txt

### canny_to_text:

python3 img_to_text.py --in_image [file-name-in.xxx] --out_file [file-name-out.xxx] --minV [int] --maxV [int]

default:
    
  * **--in_file** img.jpg
  * **--out_file** img.txt
  * **--minV** 100
  * **--maxV** 100

  >python3 img_to_text.py --in_image img.jpg --out_file img.txt --minV 100 --maxV 200



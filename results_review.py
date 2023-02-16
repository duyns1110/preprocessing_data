IN_HOME='/home/lenovo/Desktop/labelImg/results' #folder contain img and xml file after preprocessing data
OUT_HOME='/home/lenovo/Desktop/labelImg/ketqua' #folder contain random 50 imgs and 50 xml files to review
import os
from glob import glob
import shutil
from random import shuffle

shutil.rmtree(OUT_HOME)
os.mkdir(OUT_HOME)

all_im_ps=glob(os.path.join(IN_HOME,'*jpg'))
all_label_ps=glob(os.path.join(IN_HOME,'*xml'))
assert(len(all_im_ps)==len(all_label_ps))

shuffle(all_im_ps)

for im_p in all_im_ps[:50]:
   im_name=os.path.basename(im_p)
   sample_name=os.path.splitext(im_name)[0]
   label_name=f'{sample_name}.xml'
   label_p=os.path.join(IN_HOME,label_name)
   shutil.copy(im_p,os.path.join(OUT_HOME,im_name))
   shutil.copy(label_p,os.path.join(OUT_HOME,label_name))
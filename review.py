IN_HOME='/home/lenovo/Desktop/labelImg/results' #folder contain img and xml file after preprocessing data
import os
from glob import glob

all_im_ps=glob(os.path.join(IN_HOME,'*jpg'))
all_label_ps=glob(os.path.join(IN_HOME,'*xml'))
assert(len(all_im_ps)==len(all_label_ps))
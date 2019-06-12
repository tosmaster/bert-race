# -*- coding: utf-8 -*-
"""
Run EDA on a specified dataset. EDA code is written by Jason Wei and Kai Zou:
    https://github.com/jasonwei20/eda_nlp/blob/master/code/eda.py
    
@author: Jay
"""

import glob
import json
import os
import shutil
import time
import random
from eda import *

start = time.time()

# Variables
INPUT = "RACE" # the input directory
OUTPUT = "EDA_M2" # the output directory
NUM_AUG = 2 # number of augmented files to generate per randomly chosen file
ALPHA = 0.1 # how much to change each sentence
TOTAL = 2000 # total number of files to be augmented (to be added to dataset)

# read each file, copy NUM_AUG times, and replace article with eda
def augment(path):
    filenames = random.sample(glob.glob(path + "/*txt"), TOTAL)
    for filename in filenames:
        new_filename = filename[:-4] + "_" + str(0) + filename[-4:]
        os.rename(filename, new_filename)
        for i in range(1, NUM_AUG + 1):
            copy_filename = new_filename[:-5] + str(i) + new_filename[-4:]
            shutil.copyfile(new_filename, copy_filename)
        with open(new_filename, 'r', encoding='utf-8') as fpr:        
            data_raw = json.load(fpr)
            article = data_raw['article']
        aug_article = eda(article, alpha_sr=ALPHA, alpha_ri=ALPHA, 
                          alpha_rs=ALPHA, p_rd=ALPHA, num_aug=NUM_AUG)
        for i in range(NUM_AUG+1):
            write_file = new_filename[:-5] + str(i) + new_filename[-4:]
            with open(write_file, 'r', encoding='utf-8') as fpr:
                data_raw = json.load(fpr)
                data_raw['article'] = aug_article[i]
            with open(write_file, 'w', encoding='utf-8') as fpr:
                fpr.write(json.dumps(data_raw))


# first, copy the entire INPUT directory
shutil.copytree(INPUT, OUTPUT)

# run eda augmentation
train_path_h = OUTPUT + "/train/high"
augment(train_path_h)
train_path_m = OUTPUT + "/train/middle"
augment(train_path_m)        

# zip the output directory (data augmented dataset)
shutil.make_archive(OUTPUT, 'zip', OUTPUT)

end = time.time()
print("Computation time:", end - start)

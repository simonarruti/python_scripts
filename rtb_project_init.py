#!/usr/bin/env python3

from sys import argv
import shutil
import subprocess
import os

project_folder_path = '/Users/sar/Documents/rtb/projects'
project_name = argv[1]

shutil.copytree(project_folder_path + '/rtb-template', project_folder_path + '/' + project_name)

os.chdir(project_folder_path + '/' + project_name)

shutil.rmtree('.git')

subprocess.run(['make', 'install'])

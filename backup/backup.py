import sys
import os
# import shutil

def zip():
  # print(f"{os.path.basename(root_directory)}/data")
  # os.system(f"mkdir {}/data")
  os.system(f"tar -cvzf dataBackup.tar.gz {os.path.abspath('..')}/data1")
  # os.system(f"sudo rm -rf {root_directory}/data") # удаляет папку data


def unzip(path_to_data_backup):
  os.system(f"sudo rm -rf {root_directory}/data")
  os.system(f"tar -xvf {path_to_data_backup} -C {root_directory}/data")

if __name__== "__main__":
  root_directory= os.path.abspath("..")
  action = sys.argv[1]
  if action == 'zip':
    zip()
    print('Complete! Archive is in the folder with the script!')
  elif action == 'unzip':
    archive = sys.argv[2]
    if os.path.isfile(archive) and os.path.basename(archive).endswith(".tar.gz"):
      unzip(sys.argv[2])
      print('Unzip and backup successful!')
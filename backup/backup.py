import sys
import os
import shutil
from datetime import datetime

def zip():
  now = datetime.now()
  zip_name = f"{root_directory}/backup/dataBackup {now.strftime('%d-%m-%Y %H:%M')}"
  directory_name = f"{root_directory}/data"
  shutil.make_archive(zip_name, 'zip', directory_name)

def unzip(path_to_data_backup):
  os.system(f"sudo rm -rf {root_directory}/data")
  print(path_to_data_backup)
  shutil.unpack_archive(path_to_data_backup, f"{root_directory}/data")

if __name__== "__main__":
  root_directory= os.path.abspath("..")
  action = sys.argv[1]
  if action == 'zip':
    zip()
    print('Complete! Archive is in the folder with the script!')
  elif action == 'unzip':
    archive = sys.argv[2]
    if os.path.isfile(archive) and os.path.basename(archive).endswith(".zip"):
      unzip(sys.argv[2])
      print('Unzip and backup successful!')
  else:
    print('Error! First argument must be zip or unzip!')
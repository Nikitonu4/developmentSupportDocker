import sys
import os
import shutil

def zip():
  # zname = f"{root_directory}/backup/dataBackup.zip"
  # newzip=zipfile.ZipFile(zname,'w') #создаем архив
  # newzip.write(f"{root_directory}/data")

  zip_name = f"{root_directory}/backup/dataBackup"
  directory_name = f"{root_directory}/data"

  shutil.make_archive(zip_name, 'zip', directory_name)

  # os.system(f"mkdir {}/data")
  # os.system(f"tar -cvzf dataBackup.tar.gz {os.path.abspath('..')}/data1")
  # print(root_directory)
  # os.system(f"sudo rm -rf {root_directory}/data") # удаляет папку data


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
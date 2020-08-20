import os
import shutil

song_folder = "D:\\Games\\Steam\\steamapps\\common\\Beat Saber\\Beat Saber_Data\\CustomLevels\\"

folder_names = [x for x in os.listdir(song_folder)]

id_dict = {}

for fn in folder_names:
	id = fn[:4]
	if id in id_dict:
		shutil.rmtree(song_folder + fn)
		print("duplicate deleted:")
		print(fn)
	id_dict[id] = fn
import os

directory = "F:\\-100-Days-of-Code--SYED-SHAHID-NAZEER"

for i in range(1, 101):
    folder_name = f'Day{i}'
    os.makedirs(os.path.join(directory, folder_name))

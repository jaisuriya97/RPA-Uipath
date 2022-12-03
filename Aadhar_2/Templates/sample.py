import os
import gridfs
path_of_the_directory= "C:/Users/jaisu/Documents/UiPath/Aadhar_2/static"
print("Files and directories in a specified path:")
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):
        print(filename)
        
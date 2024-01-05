import os 
import readJv
'''
    this script is for read all the file in the project with extension .jv
    and then save it on filesJv.
    we will reading all the file in the list filesJv and create the new file .cpp
'''

projectPath='C:\\Users\\USER\\Fuck You\\Assets' #this is for save the path of your unity project (script folder)
currentFolder=os.getcwd() #get the current folder
pathFilesJv=[] #this is la list for save the path of the file jv
foldersPath=[] #this is for save the folder of the project 
foldersPathJv=[]
filesJv=[] #this is la list for save the file jv

def get_all_file_of_the_folder(path):
    return os.listdir(path)

def read_all_file_of_the_folder(path,files):
    #we will to read all the file of the folder
    for file in files:
        pathFile=os.path.join(path, file) #this is for create the new path of the file
        save_all_file_jv(pathFile)

def save_all_file_jv(pathFile):
    if this_file_is_a_folder(pathFile):
        read_subfolder(pathFile)
    else:
        #we will see if the file is jv
        if this_file_is_jv(pathFile):
            save_file_jv(pathFile)

def read_subfolder(pathFile):
    foldersPathJv.append(pathFile) #save the folder
    newFiles=get_all_file_of_the_folder(pathFile) 
    read_all_file_of_the_folder(pathFile,newFiles)

def save_file_jv(pathFile):
    pathFilesJv.append(pathFile) #save the path file

def this_file_is_jv(file):
    return file.endswith('.jv') #let's see if the file extension is .jv

def this_file_is_a_folder(file):
    return os.path.isdir(file) #we know if the object is a folder or a file



#-----this functions is for save the project
def read_my_project():
    global currentFolder
    #get all the file of the folder
    files=get_all_file_of_the_folder(currentFolder)
    read_all_file_of_the_folder(currentFolder,files)

def filter_address():
    #this is for delate path start
    for fileJv in pathFilesJv:
        filesJv.append(os.path.relpath(fileJv, currentFolder))

def filter_address_folder():
    #this is for delate path start
    for folder in foldersPathJv:
        foldersPath.append(os.path.relpath(folder, currentFolder))

def create_files_cpp():
    global projectPath
    #we will read the code jv and convert to cpp
    for file in filesJv:
        pathFileUnity=os.path.join(projectPath, file)
        pathFileUnity=pathFileUnity.replace('.jv','.cs') #this is for choose the extension 
        readJv.read_file(file,pathFileUnity)

def create_folders():
    for folder in foldersPath:
        #we will see if the path is of python
        if not folder == '__pycache__':
            newPathFolder=os.path.join(projectPath, folder)
            os.makedirs(newPathFolder, exist_ok=True) #create the folder in the unity project

def save_project():
    print('start')
    read_my_project()
    filter_address()
    filter_address_folder()
    create_folders()
    create_files_cpp()
    print('finish')

save_project()
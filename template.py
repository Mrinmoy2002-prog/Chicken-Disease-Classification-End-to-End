
import os
from pathlib import Path
import logging

#Logs are basically events that occured within the system like errors, user actions, system status and updates etc.,
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:') #the log gives the time when the code runs along with the message

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",        #.gitkeep is used because if we commit a empty file or folder 
    f"src/{project_name}/__init__.py",   # This __ini__.py is used in scenarios like if we want to import something from the src folder then it can be imported like a package
    f"src/{project_name}/components/__init__.py",   #Same with component package
    f"src/{project_name}/utils/__init__.py",   #Same with utils package
    f"src/{project_name}/config/__init__.py",   
    f"src/{project_name}/config/configuration.py",   
    f"src/{project_name}/pipeline/__init__.py",   
    f"src/{project_name}/entity/__init__.py",   
    f"src/{project_name}/constants/__init__.py",   
    "config/config.yaml",
    "dvc.yaml",
    "params.yml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)   # in the above list_of_files all were mentioned using a forward / but in windows we use '\' and so path converts it 
    filedir, filename = os.path.split(filepath) # this line splits the folder name (preject name) and filenme (i.e __init__.py) and stores into filedir and filename variable

# Creating a directory
    if filedir !="":
        os.makedirs(filedir, exist_ok=True) #it will create a directory if there is not one present(i.e exist_ok=true)
        #Now print a message in the logging 
        logging.info(f"Creating Directory: {filedir} for the file : {filename}")

#Creating the files eg, configuration.py etc

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #if File exists or it has size 0(means nothing is present in it)
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    else:  #If the file exists
        logging.info(f"{filename} is already exists")


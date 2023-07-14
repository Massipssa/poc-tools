
# Python project template


1. [Description](#description)
2. [Project Structure](#porject_strct)
3. [How to use it](#usage)


## 1. Description

This section describes the architecture that each python project should respect. Using this template to create
your project will help you to: 
- Run your unit tests
- Perform code quality checks using SonarQube
- ...


##@ TODO:
- the project should be created in github and user will have to specify project name
- 


## 2. Project Structure <a name="porject_strct"/>

```
project-name
     |- docs
     |- requirements
     |--|
     |  |-- requirements.txt
     |- src
     |- tests
     |- Jenkinsfile
     |- pytest.ini
     |- .flake8
     |- .gitignore
     |- .pre-commit-config.yaml
     |- sonar-project.properties
     |- setup.py
     |- REAME.md
```

Below the **breve** description of the folders and the files within the project structure.

- **docs**
  - Contains all the documents that you estimate are required or useful for someone how maybe will have
    to use your project. 
  - The files' extension within the folder **docs** can only be ``.md`` or ``.rst``.
  
- **requirements**:
    - It must contain the file `requirements.txt` within you have to specify all the dependencies' 
      names and versions which are required by your project.

- **src**
  - It must be a python package and also all the folders under **src** must be python packages too.
  - It contains all your project code, that are defined inside python files. 
    
- **tests**
  - It must be a python package.
  - It contains python code files to be used to perform, unit test, integration and functional test.
    

- **Jenkinsfile**
    - Define the **CI/CD** pipeline.   

- **README.md**
  - It contains a short description of the project's usage and utility. 
  - It may also describe how to use the project, how to install it if the installation is needed, and it can also list
    what you're planing to do in the coming releases of your project.
  
## 3. How to use it <a name="usage" />  
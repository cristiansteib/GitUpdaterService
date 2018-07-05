# Git updater service

Usado para mantener actualizado el servidor automaticamente, desde una repositorio git,
seleccionando un branch.

How to run:
----------------------------------------------------------------------
python run_updater.py -i config.ini  -d  
python run_updater.py -c /path/to/config/folder

parameters:
-----------------------------------------------------
| Help        | Param | Param extended         | arg required |
| ------------- |-------------| -----| ----|
| show help text   | -h  |--help  | No |
| specify the config file      | -i   | --ini|  /path/to/config.ini |
| specify the folder of configs | -d      | --config-directory|  /path/to/config/folder/ |
| show what is going on| -v | --verbose| No|
| show very detailed what is going on| -vf | --verbose-full |No | 
| Daemonize | -d | --daemonize |No |   

The configs files 
-------------------------------------------------------------------
[ProjectName] : Set the project name. **Mandatory**   
path : Set the path where is located the with project. **Mandatory**  
branch : Set the branch to update. **Mandatory**  
pre_update: A command to run before update, if update was needed.  
post_update: A command to run after update.   

 Config example
--------------------------------------------------------------------

```ini
[ProjectName]
path=/absolute/path/to/project
branch=master
pre_update=echo "Hello World" > ~/file.file
post_update=echo "update done" >> ~/file.file
```

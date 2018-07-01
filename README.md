# updaterDaemon

Usado para mantener actualizado el servidor automaticamente, desde una repositorio git,
seleccionando un branch.

The configs files 
-------------------------------------------------------------------
[ProjectName] : Set the project name, **Mandatory**   
path : Set the path where is located the with project **Mandatory**  
branch : Set the branch to update **Mandatory**  
 
 Config example
--------------------------------------------------------------------

```ini
[ProjectName]
path=/absolute/path/to/project
branch=master
pre_update=echo "Hello World" > ~/file.file
post_update=echo "update done" >> ~/file.file
```

How to run:
----------------------------------------------------------------------
python run_updater.py --ini config.ini


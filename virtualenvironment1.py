#create a folder named python-venv, open it in terminal
# type python -m venv myenv and press enter in terminal, this creates a new folder inside the folder
# then type .\myenv\Scripts\Activate

#if says script running is disabled on this system type Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser ,
# (note that even space between dash and uppercase and lowercase of the letter matters )
# then type .\myenv\Scripts\Activate again
# you need to install all the libraries required for it, like pandas and others
# type pip install pandas to install it
# if you want to install specific versions
# type pip install pandas==1.4.4  (1.4.4 is the version of that library)
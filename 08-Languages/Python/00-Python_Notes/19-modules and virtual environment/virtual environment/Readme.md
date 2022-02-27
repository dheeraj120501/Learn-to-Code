- A virtual environment is a tool or an aid provided to us by Python to keep the dependencies that we have utilized earlier in a few projects, constant.
- Virtual Environment saves the current state of our compiler along with the state of their modules and libraries.
- We can also install different packages and “dataframes” in our virtual environment.

- To create a virtual environment we can also use:

  - `py -m venv virtualenv_name` // to create a new virtual environment named virtualenv_name

- Once created we need to activate it to start using that env for this just run the activate file in the env folder through shell.

  - `.\virtualenv_name\Scripts\activate`
  - `(virtualenv_name)$ deactivate` // to deactivate the env

- requirements.txt is just like package-lock.json that keeps the record of all the modules installed in that virtual environment.

  - `pip freeze > requirement.txt` // do this in same dir. of vir. env.

- pip install package_name == version // to install a package's specific version
- pip install -r .\requirements.txt // to install all packages of requirement txt file
## Summary
This is to do a JSON-Yaml conversion for system data downloaded from OneView. Converting to an usable playbook.

## Requirements:
- Python2
- Python-pip package manager
- virtualenv
> **_NOTE:_** Both Python3 and Python3-pip can be installed from the Linux OS pakcage manager, such as apt-get and yum. Virtualenv can be installed from Pip. 

## Setting up the environment
> **_NOTE:_** According to the [Control Machine Requirements section](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#control-machine-requirements) in the Ansible documentation, Window is not supported.

1. In terminal, git clone this repo.
```
$ git clone git@github.hpe.com:jih-tsen-nat-lin/oneview-ansible-openshift-integrations.git
```
2. Create a Python 2.7 virtual environment.
```
$ virtualenv project-env --python /bin/bin/python
```
3. Activate the environment, and then pip install the dependencies from the requirments file. 
```
$ source project-env/bin/activate
$ pip install -r requirements.txt
```

4. To run the code:
```
(project-env)$ python main.py
```

## Resources
- [Ansible Modules for HPE OneView](https://github.com/HewlettPackard/oneview-ansible)
- [HPE OneView SDK for Python](https://github.com/HewlettPackard/python-hpOneView#installation)
- [Image Streamer Reference Architectures](https://github.com/HewlettPackard/image-streamer-reference-architectures/tree/master/RC-RHEL-OpenShift-Synergy)
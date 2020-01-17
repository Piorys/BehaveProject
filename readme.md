# Python Automation


## Overview

This framework is designed to help you quickly start with implementing automation within Your project. It's based on [Behave Framework](https://behave.readthedocs.io/) 
which facilitates [Behaviour Driven Development](https://en.wikipedia.org/wiki/Behavior-driven_development) principles with [Selenium for python](https://selenium-python.readthedocs.io/) 
which allows to mimic user actions on any given website. 

Framework structure goes as follows:

![Structure](./documentation/Structure.png)

## Instalation

##### Prerequisites:
- Python 3.7 - [Installation](https://www.python.org/downloads/)
- PIP version 18.7 - [Installation](https://pip.pypa.io/en/stable/installing/)
- Chromedriver - [Installation](https://chromedriver.chromium.org/getting-started)
- Google Chrome - [Installation](https://www.google.com/chrome/)
- GIT - [Installation](https://git-scm.com/downloads)


##### Get repo
``
git clone https://bitbucket.org/Piorys/pythonautomation.git
``

#### Install requirements
``
pip install -r requirements.txt
``

## Execution

In order to execute all tests:  
``
behave
``  
  
To execute tests by tag  
``
behave --tags=@tagname
``
  
Currently 2 features are created:
 - TwitterPosts  
 -- T.1.1 - Create Post  
 -- T.1.2 - Create Post Widget  
 -- T.1.3 - Delete Tweet  
 -- T.1.4 - Post character limit  
 - TwitterProfile  
 -- T.2.1 Edit Profile Page  
 -- T.2.2 Adding Bio  
 -- T.2.3 Adding Location  
  
 For more information about scenarios please refer to feature files located in ```features/``` directory
 
## Configuration

Configuration can be found in ```TestConf.py``` file, where following preferences can be set:
- DefaultTimeout
- Output directory for logger module
- Logger file name
- Screenshot directory
- Environment
- Headless execution

## Artifacts

- Log output in /output directore
- Screenshots on failed tests in ```/output/screenshots``` directory

## Known issues

- Twitter tends to provide captcha challenge (typically once a day) to test account, 
this situation requires manual user input and can not be omited
- Fields in edit profile page are not cleared, this requires further investigation



## About the Project
This project includes Selenium Python Scripts to Automate & Update Recruitment Posts for
Life Commnications Group


### Dependencies
List of frameworks/librarys used to create this project:

* [Python](https://www.python.org/downloads/)
* [Selenium](https://selenium-python.readthedocs.io/installation.html)
* [ChromeDriver](https://chromedriver.chromium.org/downloads)



## Getting Started
To run the script, follow the steps below

### Prerequisites
* [Google Chrome](https://www.google.com/chrome/)
1. Create a new profile on chrome.
2. Save the login details to [https://en-gage.net/](https://en-gage.net/) and [https://employers.indeed.com/](https://employers.indeed.com/) on your new chrome profile.



### Installation
Open the file `engage.py` and edit the lines below with our chrome profile path.<br>
*(your chrome profile path can be found at [chrome://version/](chrome://version/))*
```python
options.add_argument('--user-data-dir=...')
options.add_argument('--profile-directory=...')
```


## Usage
Run `engage.py`
```python
py engage.py
```


## Contributing
Contributions are welcomed and greatly appreciated!

If you have any suggestions, please fork the repo and create a pull request or open an issue. 

Thanks!


## License
Distributed under the MOOSHKID License. See LICENSE.txt for more information.


## Authors
Masa Yamanaka - yamanaka@lcom-group.jp

Project Link: [https://github.com/mooshkid/lifecom](https://github.com/mooshkid/lifecom)
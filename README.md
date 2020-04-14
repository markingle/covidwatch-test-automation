# CovidWatch Test Automation

This repository contains an Appium automation framework for testing the CovidWatch iOS and Android phone app.
Python is used to drive app automation using Appium. Pytest is used as the testing framework.

## Installation

User must have [NodeJS](https://nodejs.org/en/download/) installed, then [Appium](http://appium.io/) must be installed via npm:

```bash
npm install -g appium
```

Android studio is also recommended for virtual Android images as well as Android device manager (adb).

Python version 3.6.1 is used for development, please refer to requirements.txt to install necessary packages.

## Usage

Devices to test need to have a config file in the `./tests/config` directory.

To find what should go in the ```deviceName``` and ```udid``` fields, use the ```adb``` command in terminal to find 
connected android devices.

To find what should go in the ```appPackage``` and ```appActivity``` fields, please see 
[this](http://www.automationtestinghub.com/apppackage-and-appactivity-name/) web page.

Run all tests with:
```bash
pytest test_app.py
```

Run specific tests with:
```bash
pytest test_app.py::test_func
```
Where `test_func` can be any of the available test functions.

## Contributing
Contribution is welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[Apache](https://choosealicense.com/licenses/apache-2.0/)
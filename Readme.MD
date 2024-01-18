# Speed Logger

A simple speed logger for the [Speedtest CLI](https://www.speedtest.net/apps/cli) written in Python.
The User can set a time interval in which the speed is logged to a CSV file.
A simple plotter is included to visualize the data.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install the project, follow these steps:

```bash
git clone https://github.com/mrdiamonddirt/speed-logger.git

cd speed-logger

pip install -r requirements.txt
```

## Usage

To use the project, follow these steps:

open a terminal in the project folder and run the following command:

```bash
python speed-logger.py
```
this will start the speed logger giving you the option to set the time interval in which the speed is logged.

To create a plot of the data, run the following command:

```bash
python plotter.py
```

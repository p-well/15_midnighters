# Night Owls Detector

The intent of the program is to find midnight owls among [DEVMAN.org](https://devman.org) training course students. <br />

Script connects to Devman server via [API](https://devman.org/api/challenges/solution_attempts/?page=1), retrieves and parses data and prints out a list of students who have sent their <br />
tasks for mentor's check in time interval 0:00 a.m - 6:00 a.m.

Pavel Kadantsev, 2017. <br/>
p.a.kadantsev@gmail.com

# Installation

Python 3.5 should be already installed. <br />
Clone this repo on your machnine and install dependencies using command ```pip install -r requirements.txt``` in CLI. <br />
It is recommended to use virtual environment.

# Usage

To execute the script use the following command in CLI: ```python seek_dev_nighters.py```. <br />
CLI encoding changing may be required for correct script running on Windows platform: for UTF-8 encoding use  <br /> ```chcp 65001```

# Example of Script Launch

```
(env) C:\projects\devman\15_midnighters>python seek_dev_nighters.py

Retrieving midnight users from Devman.org database. Please wait.

Done! Here is a list of devman owls:

1. irinanizova0
2. LizzaVeta
3. lekcrg
4. AntonKupranis
5. SergeiKhrustalev
6. АлексейЦыкунов
7. СашаБратчиков
8. ЕвгенийНечуй-Ветер
9. ВадимТатар
10. andrewnorilsk
11. СергейИванов
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

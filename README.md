<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Trading Suggestor <a  name = "about_the_project"></a>](#trading-suggestor-)
  - [Directory Structure <a  name = "directory_structure"></a>](#directory-structure-)
  - [Requirements <a  name = "requirements"></a>](#requirements-)
  - [Deployment <a  name = "deployment"></a>](#deployment-)
  - [Contact <a  name = "contact"></a>](#contact-)
---


<!-- ABOUT THE PROJECT -->
# Trading Suggestor <a  name = "about_the_project"></a>

This Trading Suggestor repository analyses any specific trading market based on the particular days, such as what happened every Monday for the last 12 weeks. The application uses data from [yahoo finance](https://finance.yahoo.com/). 


<!-- DIRECTORY STRUCTURE -->
## Directory Structure <a  name = "directory_structure"></a>

Here's a project's directory structure:

```text
trading-suggestor
├── diagram						# System architecture
│   ├── class_diagram.svg
│   ├── plantuml.txt
│   └── usecase.svg
├── individual_days_series.py	# Creates a set of days
├── README.md
└── yahoo_finance.py			# Main program
```


<!-- REQUIREMENTS -->
## Requirements <a  name = "requirements"></a>

-  [Python >= 3.7 <a href="https://www.python.org/downloads/"> </a>](python_download)

 
<!-- DEPLOYMENT -->
## Deployment <a  name = "deployment"></a>

- Activate python virtual environment **or** install packages on local system:
	- `source venv/bin/activate` **or**,
	- `pip3 install –r requirements.txt`
-   `python3 yahoo_finance.py`


<!-- CONTACT -->
## Contact <a  name = "contact"></a>

**Azizul Hakim Shakil** - [@ShakilAzizul](https://twitter.com/ShakilAzizul) - azizulhakim.shakil18@gmail.com

Project Link: [https://github.com/shakil18/Trading-Suggestor](https://github.com/shakil18/Trading-Suggestor)

# CareerTime

## Overview
CareerTime is a simple Python application that calculates the total full-time work experience (in years) for a given list of LinkedIn profiles. It uses sample data from a JSON file to simulate Coresignal API responses.

**Key Features:**
- Extract LinkedIn profile IDs from URLs.
- Load sample Coresignal-like data from a JSON file.
- Calculate total years of work experience, accounting for partial and ongoing roles.
- Print the results in JSON format.

## Setting-up
* Clone the repository:
   ```bash
   git clone https://github.com/orkhanshirin/career_time.git
   ```
* 
   ```bash
   cd career_time
   ```

## Usage
1. Put your LinkedIn profile URL into data/input_urls.txt (one URL per line).
2. Ensure data/sample_profile.json contains a profile's experience data that matches the LinkedIn ID you're testing.
3. Run the program:
   From the project root folder:
    ```bash
    python3 -m src.career_time.main
    ```
4. The output will be printed to the console in JSON format.

## TODO

This project is partially implemented to showcase the main logic of extracting work experience of talents in a given JSON data.
You can see the main ideas to expand, and improve the functionality, and decrease the cognitive complexity of the project:

[TODO list](TODO.md)

## Project Structure

`src/career_time/` contains all source code.

`data/` contains input and sample data files.

`tests/` contains all test files and fixtures(if any).

```tree
career_time/
├─ README.md
├─ .gitignore
├─ pyproject.toml
├─ src/
│  ├─ career_time/
│  │  ├─ __init__.py
│  │  ├─ main.py
│  │  ├─ experience.py
│  │  ├─ data_providers.py
├─ data/
│  ├─ input_urls.txt
│  └─ sample_profile.json
└─ tests/
```
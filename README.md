# Vision Source Scraper

This project is part of [Project Upwork](https://github.com/toludaree/project-upwork). This is the job [link](https://www.upwork.com/jobs/~011a29a01aebe10c0a).

## Job Description
For the attached list of 51 [URLs](./urls.txt) please do the following.

1. Go to each page of results. Some URLs will have lots of page results (15+) while some will have few page results (4 or less).

2. For the results on each page, scrape the following information for each business listed:
  - Business Name
  - Doctor Name
  - Address
  - Phone Number
  - Website (if listed)

3. Organize this information into a CSV or Excel file that we can access.

## Result Schema
- business_name
- doctors
- address 
- phone_number
- website

## Example Data (in JSON)
```json
{
    "business_name": "Drs. Farkas, Kassalow, Resnick & Associates",
    "doctors": [
        "Dr. Susan Resnick",
        "Dr. Jordan Kassalow",
        "Dr. Kevin Rosin",
        "Dr. Kevin Patrizio"
    ],
    "address": "30 East 60th Street, Suite 201; New York, NY 10022",
    "phone_number": "(212) 355-5145",
    "website": "http://www.eyewise.com"
}
```

## Evolution


## Reproducing

### Requirements
- Python (>= 3.10)

### Setup
- Clone the reposiory
    ```bash
    git clone https://github.com/toludaree/visionsource-scraper.git
    ```
- Create a python virtual environment and activate it.
    ```bash
    python -m venv .venv

    # Activate
    .venv/Scripts/activate     # Windows
    source .venv/bin/activate  # Unix
    ```
- Install required libararies through  [requirements.txt](./requirements.txt)
    ```bash
    pip install -r requirements.txt
    ```

### Scrape away
- Naviagte to the [visionsource](./visionsource/) directory.
    ```bash
    cd visionsource/
    ```
- Activate the `businesses` spider with `scrapy crawl`.
    ```bash
    scrapy crawl businesses -O businesses.json
    ```
    - This saves the result as a JSON file. You can also save as a CSV or XML file.



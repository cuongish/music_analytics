### Description
   - A quick analysis on music consumption data and feed-station mapping.

### Virtual environment
  - Create virtual env
```bash 
virtualenv -p python3 venv
```

### How to Run it
1. Activate the virtualenv
    ```bash
       source venv/bin/activate
    ```
1. Install requirements:
    ```bash
       pip install -r requirements.txt
     ``` 
1. Load data into SQLite.db:
    ```bash
       python main.py
     ```
1. Open analysis.ipynb to see the report:
    ```bash
       jupyter notebook analysis.ipynb
     ```
   
### TODO improvement:

As to optimize for minimum dependencies, SQLite is the database of choice. The lack of support for timezone in SQLite is thus dealt 
with by adding/subtracting hours.

Handling of timezone is more elegantly dealt with in Postgres for example.
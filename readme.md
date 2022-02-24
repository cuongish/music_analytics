### Description
   - A quick analysis on music consumption data and feed-station mapping

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
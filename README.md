# Set up Guide

## Note
If you are testing it out on other excel or csv files,
please remove this line of code from app.py as this removes the last row of data

``` bash
df_data = df_data.iloc[:-1]
```
In Red Wine mock dataset, the last row is the total sales, which messes up the dataframe

Thank you and have a nice day

## Virtual Environemnt

Create virtual environment
``` bash
python -m venv .venv
```

Activate virtual environment
``` bash
.venv/Scripts/Activate.ps1
```

## Install dependencies
``` bash
pip install -r requirements.txt
```

## API key
Put in your own OpenAI API Key in .env file

## Run Application
``` bash
streamlit run app.py
```
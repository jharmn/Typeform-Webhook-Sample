# Typeform Webhook Sample API

This is a sample API supporting [Typeform Webhooks](https://www.typeform.com/help/webhooks/). This should not be considered production deployable, and is not supported by Typeform. It is only intended to show how webhooks work in a simple example.

## Setup

This sample uses Python and Flask. Virtualenv and PIP are recommended to resolve requirements.

### Create Typeform

Create new Typeform in your workspace, based on Event Registration template. Replace question IDs in `app.py` with your IDs (best to use requestb.in to inspect your data to determine this). 

```
r_name = self.get_answer(answers, '21524209', 'text') # Replace 21524209 with your IDs
```

### Create database

``` 
pip install -r requirements.txt
python create_db.py
```

### Start API

Starts on port 5000 by default.

```
IP_ADDRESS=<your desired IP> python app.py
```

## Run Tests

WARNING: This will delete local database

```
python run_tests.py
```

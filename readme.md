# SetUp
## Create a virtual environment

```
python3.10 -m venv .venv
source .venv/bin/activate
```

## Install requirements
```
pip install -r requirements.txt
```

## Init proyect

```
flask run
```

### Docker instructions

```
docker build -t <nombre> .
docker run -dp 5005:5000 -w /app -v "$(Get-Location):/app" odmoreno/flask-api
```

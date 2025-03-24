## Activar VEnv

```
source .venv/bin/activate
```

## Iniciar proyecto

```
flask run
```

### Intrucciones para docker

```
docker build -t <nombre> .
docker run -dp 5005:5000 -w /app -v "$(Get-Location):/app" odmoreno/flask-api
```

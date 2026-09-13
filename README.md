# Shahadab Sheikh Portfolio

Enhanced Flask portfolio with responsive UI, theme toggle, animations, project sections, security headers, health check, and production Gunicorn support.

## Run locally
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Deploy
Use the included `Procfile`:
```text
web: gunicorn app:app
```

Set `SECRET_KEY` in production and add your assets under `static/`.

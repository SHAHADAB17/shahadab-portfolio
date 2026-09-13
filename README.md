# Shahadab Sheikh Portfolio

A Flask-powered portfolio website for Shahadab Sheikh.

## Run locally

```bash
python -m venv venv
```

### Windows
```bash
venv\Scripts\activate
```

### macOS/Linux
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

Open http://127.0.0.1:5000

## GitHub

Upload this project to a GitHub repository.

## Deployment

This project includes `requirements.txt` and `Procfile` for deployment platforms that support Flask and Gunicorn.

## Assets

Place these files in the project root's `static/` folder if you have them:

- `profile.jpg`
- `Shahadab_Sheikh_Resume.pdf`

Place certificate PDFs in `static/certificates/` and update their paths in `templates/index.html`.

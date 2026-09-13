import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY", "change-this-in-production"),
    TEMPLATES_AUTO_RELOAD=os.environ.get("FLASK_ENV") == "development",
)

@app.after_request
def add_security_headers(response):
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("Permissions-Policy", "geolocation=(), microphone=(), camera=()")
    response.headers.setdefault("Content-Security-Policy",
        "default-src 'self' https:; img-src 'self' data: https:; "
        "style-src 'self' 'unsafe-inline' https:; script-src 'self' 'unsafe-inline' https:; "
        "font-src 'self' https:; connect-src 'self' https:; frame-ancestors 'self';")
    return response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify(status="ok", service="shahadab-portfolio")

@app.errorhandler(404)
def not_found(error):
    return render_template("index.html"), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("FLASK_DEBUG") == "1")

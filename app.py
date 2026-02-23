from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return {"message": "Zero Trust Demo running"}

if __name__ == "__main__":
    app.run()

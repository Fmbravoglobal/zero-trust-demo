from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def home():
    role = request.args.get("role", "user")

    if role == "admin":
        return {"access": "allowed", "reason": "admin role"}
    else:
        return {"access": "denied", "reason": "not admin"}

if __name__ == "__main__":
    app.run()

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"message": "Hello, Flask + SQLite + Docker!"})

def main():
    print("Hello World")

if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port=5000)

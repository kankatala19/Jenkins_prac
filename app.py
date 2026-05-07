from flask import Flask, jsonify

app = Flask(__name__)

# Global counter variable
counter = 0


@app.route("/")
def home():
    return "Jenkins CI/CD Working!"


# Increment counter
@app.route("/increment")
def increment():
    global counter
    counter += 1

    return jsonify({
        "message": "Counter incremented",
        "counter": counter
    })


# Decrement counter
@app.route("/decrement")
def decrement():
    global counter
    counter -= 1

    return jsonify({
        "message": "Counter decremented",
        "counter": counter
    })


# View current counter
@app.route("/counter")
def get_counter():
    return jsonify({
        "counter": counter
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
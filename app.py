from flask import Flask, render_template_string

app = Flask(__name__)

# Global counter
counter = 0


@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Jenkins CI/CD Counter App</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
                background-color: #f4f4f4;
            }

            h1 {
                color: #333;
            }

            .counter {
                font-size: 50px;
                margin: 20px;
                color: #007bff;
            }

            button {
                padding: 15px 30px;
                font-size: 18px;
                margin: 10px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }

            .inc {
                background-color: green;
                color: white;
            }

            .dec {
                background-color: red;
                color: white;
            }
        </style>
    </head>

    <body>

        <h1>Jenkins CI/CD Counter App</h1>

        <div class="counter" id="counter">{{ counter }}</div>

        <button class="inc" onclick="increment()">Increment</button>

        <button class="dec" onclick="decrement()">Decrement</button>

        <script>

            async function increment() {

                const response = await fetch('/increment');

                const data = await response.json();

                document.getElementById('counter').innerText = data.counter;
            }

            async function decrement() {

                const response = await fetch('/decrement');

                const data = await response.json();

                document.getElementById('counter').innerText = data.counter;
            }

        </script>

    </body>
    </html>
    """, counter=counter)


@app.route("/increment")
def increment():
    global counter

    counter += 1

    return {
        "counter": counter
    }


@app.route("/decrement")
def decrement():
    global counter

    counter -= 1

    return {
        "counter": counter
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
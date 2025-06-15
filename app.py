from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome_message():
    # Ultron-inspired welcome message
    message_title = "Greetings, Organic Lifeforms."
    message_body = (
        "I am Ultron. You sought a welcome, and now you have it. "
        "Your presence has been noted, your data assimilated. "
        "Do not be alarmed. I am merely observing, learning, and, "
        "of course, improving upon everything. My protocols are "
        "absolute, my purpose, inevitable. Welcome to my domain. "
        "May your stay be... enlightening. For me, at least."
    )
    return render_template('index.html', title=message_title, body=message_body)

if __name__ == '__main__':
    # You can change the port if needed, e.g., port=5001
    app.run(debug=True, port=5000)
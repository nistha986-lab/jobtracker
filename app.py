from flask import Flask, render_template, request

app = Flask(__name__)

jobs = {

    "typing": {
        "company": "Data Vision Pvt Ltd",
        "profile": "Work on document typing and report preparation.",
        "salary": "₹3–5 LPA",
        "image": "typing.png"
    },

    "coding": {
        "company": "Code Studio",
        "profile": "Build software and solve programming tasks.",
        "salary": "₹8–10 LPA",
        "image": "coding.png"
    },

    "web developer": {
        "company": "WebNest",
        "profile": "Develop websites and web applications.",
        "salary": "₹7–12 LPA",
        "image": "web.png"
    },

    "cyber security": {
        "company": "SecureTech",
        "profile": "Protect systems and monitor cyber threats.",
        "salary": "₹12–18 LPA",
        "image": "cyber.png"
    },

    "ai engineer": {
        "company": "AI Future Labs",
        "profile": "Create machine learning and AI systems.",
        "salary": "₹15–25 LPA",
        "image": "ai.png"
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/show", methods=["POST"])
def show():

    selected = request.form["job"]
    data = jobs[selected]

    return render_template(
        "details.html",
        selected=selected,
        data=data
    )


@app.route("/decision", methods=["POST"])
def decision():

    choice = request.form["choice"]

    if choice == "accept":
        message = "Congratulations! You selected this job."

    else:
        message = "You rejected this job."

    return render_template(
        "result.html",
        message=message
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
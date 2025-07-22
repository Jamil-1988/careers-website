from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scintist',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Front End Engineer',
        'location': 'Remote',
    },
    {
        'id': 4,
        'title': 'Cakend Engineer',
        'location': 'San Fransisco, USA',
        'salary': '$. 120,000'
    },
]


@app.route("/")
def hello_wordl():
    return render_template("home.html", jobs=JOBS, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs(): 
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
 
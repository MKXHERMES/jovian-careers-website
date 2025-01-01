from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)

JOBS = [{'id': 1,
         'title': 'Data Analyst',
         'location': 'Bengaluru, India',
         'Salary': 'Rs.15,00,000'},
        {
         'id': 2,
         'title': 'Data Scientist',
         'location': 'Mumbai, India',
         'Salary': 'Rs.18,00,000'
        },
        {
         'id': 3,
         'title': 'Frontend Engineer',
         'location': 'Remote',
         'Salary': 'Rs.12,00,000'
        },
        {
         'id': 4,
         'title': 'Backend Engineer',
         'location': 'San Francisco, USA',
         'Salary': '$1,20,000'
        }]

@app.route("/")
def hello_jovian():
    return render_template('home.html', Jobs=JOBS, company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


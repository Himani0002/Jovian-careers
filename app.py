from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'SEO',
        'location': 'Remote',
        'salary': 'Rs. 16,00,000'
    },
]


@app.route('/')
def home():
    return render_template('home.html', jobs=Jobs, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)


if __name__ == '__main__':
    app.run(debug=True)

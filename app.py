from flask import Flask,render_template,jsonify

app=Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'Data analyst',
    'location':'kolkata',
    'salary':'rs 1000000'
  },
  {
    'id':2,
    'title':'Data Engineer',
    'location':'kolkata',
    'salary':'rs 1200000'
  },
  {
    'id':3,
    'title':'AI ngineer',
    'location':'kolkata',
    'salary':'rs 1500000'
  },
  {
    'id':4,
    'title':'Backend developer',
    'location':'kolkata'
  }
]
@app.route("/")
def hello():
  return render_template("home.html",jobs=JOBS,company_name='xyz')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)
  
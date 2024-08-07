from flask import Flask,render_template
app=Flask(__name__)
JOBS = [
    
  {
    "id": 1,
    "title": "Software Engineer",
    "location": "Bangalore, Karnataka",
    "salary": "₹12,00,000"
  },
  {
    "id": 2,
    "title": "Data Analyst",
    "location": "Mumbai, Maharashtra",
    "salary": "₹8,50,000"
  },
  {
    "id": 3,
    "title": "Project Manager",
    "location": "Hyderabad, Telangana",
    "salary": "₹9,50,000"
  },  
  {
    "id": 4,
    "title": "Marketing Specialist",
    "location": "Chennai, Tamil Nadu",
    "salary": "₹7,50,000"
  }

]
@app.route('/')
def home():
    return render_template ('home.html',jobs=JOBS)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
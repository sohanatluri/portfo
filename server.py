from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database:
        Name = data['name']
        Email = data['email']
        Number = data['phone']
        Message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([Name,Email,Number,Message])




@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
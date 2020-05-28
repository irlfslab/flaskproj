# Create our flask main python file, naming convention: app.py 

from flask import Flask, render_template, request, json, flash

app = Flask(__name__)
app.secret_key = 'secretkey1'

# A function called index
@app.route("/")  
def index():    
    title = "Fresh Bakery Home"
    return render_template("index.html", title=title)

# A function called order
@app.route('/order')
def order():    
    title = "Fresh Bakery Order"
    return render_template("order.html", title=title)

# A function called contact
@app.route('/contact')
def contact():
    data = []
    with open("data/workshop.json", "r") as json_data:
        data = json.load(json_data)
    title = "Fresh Bakery Contact us"
    return render_template("contact.html", title=title, workshop=data)

# A function called process
@app.route('/process', methods=["POST"])
def process():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    phone = request.form['phone']
    email = request.form['email']
    pickday = request.form['pickday']
    cakes = request.form.getlist('cakes') 
    fmsg = request.form['fmsg']
    field_is_empty=False 
    name_invalid=False
    phone_invalid=False
    
    if not cakes:
        return render_template('order.html',field_is_empty=True, f_name=firstname, l_name=lastname, email=email, phone=phone)
    
    if not firstname.isalpha() or not lastname.isalpha():
        return render_template('order.html', name_invalid=True, f_name=firstname, l_name=lastname, email=email, phone=phone)
    elif not phone.isnumeric() or not len(phone) == 10:
        return render_template('order.html', phone_invalid=True, f_name=firstname, l_name=lastname, email=email, phone=phone) 
    else:
        return render_template('process.html',f_name=firstname, l_name=lastname, phone=phone, email=email, cakes=cakes, pickday=pickday, fmsg=fmsg)
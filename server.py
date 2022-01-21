from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

all_checkouts=[]

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST','GET'])         
def checkout():
    # print(request.form)
    checkout_info={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'student_id':request.form['student_id'],
        'strawberry':request.form['strawberry'],
        'raspberry':request.form['raspberry'],
        'apple':request.form['apple'],
    }
    all_checkouts.append(checkout_info)
    count = int(request.form['strawberry'])+int(request.form['raspberry'])+int(request.form['apple'])
    print(f"Cobrando a {checkout_info['first_name']} por {count} frutas")
    return render_template("checkout.html",  checkout_info = checkout_info)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
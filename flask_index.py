from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")

#in the function return render_template(index.html)

def first_webpage() :
    name = 'Flask'

    #pass the variable in the template
    
    return render_template("/index.html", index_variable=name)


app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("home.html")
    
# @app.route("/about/")
# def about():
#     return render_template("about.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):

    usuarios = ['gabriela', 'enzo', 'donizete', 'larissa', 'lucas', 'danton']

    if nome_usuario in usuarios:

        return render_template("acesso.html", nome_usuario = nome_usuario)
            
    else:
        return render_template("acesso.html", nome_usuario)
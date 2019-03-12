from flask import Flask, render_template, request
app = Flask(__name__)

db={"usuario":"gonzalez.etec@hotmail.com", "senha":'55053683g'}

def usuario_existe(email):
	if(email == db['usuario']):
		return True
	else:
		return False

def testa_senha(user, senha):
	if(user == db['usuario'] and senha == db['senha']):
		return True
	else:
		return False

@app.route("/")
def student():
	return render_template("login.html")
	
@app.route("/registrar", methods=['GET', 'POST'])
def login_result():
	if request.method == 'POST':
		result = request.form
		print(result)
		return render_template("login.html", result)
	else:
		return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		result = request.form


		response = {"status":"correto"}
		if usuario_existe(result['email']) == True:

			if testa_senha(result['email'], result['senha']) == True:
				
				return render_template('sucesso.html', response=response)
			
			else:
				response['status'] = "senha_incorreta"
				return render_template("sucesso.html", response=response)
		
		else:
			response['status'] = "usuario_incorreto"
			return render_template("sucesso.html", response=response)
	
	
if __name__ == '__main__':
	app.run(host="0.0.0.0", debug = True)


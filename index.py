from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail,Message

app = Flask(__name__)

#configuraciones del servidor y las rutas de la páginas html y css
app.secret_key = "mysecretkey"

@app.route('/')

def home():
	return render_template("index.html")

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'correopagina.advanceclean@gmail.com'
app.config['MAIL_PASSWORD'] = "pescarpescarpescarcarpashaymuchasenlaciudad" #as
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SLL'] = False  
mail = Mail(app)



#ruta para enviar mensajes a mi correo
@app.route('/send_message', methods=['GET','POST'])
def send_message():
	if request.method == 'POST':
		email = request.form['email']
		subject = request.form['subject']
		msg = request.form['message']
		number = request.form['number']

		message = Message(subject, sender=email, recipients=['correopagina.advanceclean@gmail.com'])
		message.body =  email+ "\n" + subject+ "\n" + number + "\n" + msg 
		mail.send(message)
				
		return render_template("resultado.html")



if __name__ == "__main__":
	app.run(host="127.0.0.1",port=8000,debug = True)
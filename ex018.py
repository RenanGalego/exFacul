""" Envio de E-mail """
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#criação de um objeto de mensagem
msg = MIMEMultipart()
textoMsg = "Enviado do Pyhton"

#parâmetros
senha = "Karytta281163@"
msg['from'] = "devgalego03@gmail.com"
msg['to'] = "renangalego.alves@gmail.com"

#criação do corpo da mensagem
msg.attach(MIMEText(textoMsg, 'plain'))

#criação do serviido
servidor = smtplib.SMTP('smtp.gmail.com: 587')
servidor.starttls()

#login na conta para envio
servidor.login(msg['from'],senha)

#envio da mensagem
servidor.sendmail(msg['from'], msg['to'], msg.as_string())

#encerramento do servidor
servidor.quit()
print("Mensagem enviada com Sucesso!")
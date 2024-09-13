"""6. Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.
"""
login = input("Login - ")
senha = input("Senha - ")
while login != "admin" or senha != "admin123":
    print("Acesso negado. Login ou senha incorretos. Tente novamente.")  
    login = input("Login - ")
    senha = input("Senha - ")
print("Acesso permitido. Bem-vindo.")

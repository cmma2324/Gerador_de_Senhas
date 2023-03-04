
from random import choice
import string

def gerador_de_senha(tamanho_da_senha): 
  caracteres = string.ascii_letters + string.digits + string.punctuation
  senha_segura = ''
  for i in range(tamanho_da_senha):
    senha_segura += choice(caracteres)
    
  return senha_segura
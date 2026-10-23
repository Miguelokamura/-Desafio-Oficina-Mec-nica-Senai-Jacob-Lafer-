"""Testar a conexão com o banco de dados."""
from db import testar_conexao 
try:
    print("Conexão OK:", testar_conexao())
except Exception as e:
    print("Erro na conexão:", e)
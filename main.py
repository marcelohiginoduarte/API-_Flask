import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/homepage')
def homepage()
    tabela = pd.read_csv('arquivo.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas':total_vendas}
    return jsonify(resposta)





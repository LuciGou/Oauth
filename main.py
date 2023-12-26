from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/obter-token', methods=['GET'])
def obter_token():
    code = request.args.get('code')
    state = request.args.get('state')

    if not code or not state:
        return jsonify({'error': 'Parâmetros code e state são obrigatórios'}), 400

    # Dados necessários para o POST
    data = {
        # Adicione aqui os dados necessários para a obtenção do token
        # Por exemplo, dados de autenticação ou outros parâmetros exigidos pela API
        # Exemplo hipotético:
        'client_id': 'SEU_CLIENT_ID',
        'client_secret': 'SEU_CLIENT_SECRET',
        'grant_type': 'authorization_code',
        'code': code,
        'state': state,
    }

    try:
        # Faz a requisição POST para obter o token
        response = requests.post('https://www.bling.com.br/Api/v3/oauth/token', data=data)

        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'Erro ao obter o token'}), response.status_code
    except requests.RequestException as e:
        return jsonify({'error': f'Erro na requisição: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

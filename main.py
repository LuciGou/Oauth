from flask import Flask, request, jsonify
import requests

app = Flask(AuthFlashBling)

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
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '1.0',
        'Authorization': 'Basic OTQwM2M2MzkyYTAxZGY2MzgyZDZiMTVjNWMxMmNkOTI4Y2U3OGE3NjplMDNmODJjMTI5Njk2ZTA4NmM2OGJmYTdlOTBkZDA2OWRhZDliNjJjYTZiYmUwN2I2NTA2OGQyMjVmOWE=',
        'grant_type': 'authorization_code',
        'code': code,
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

if AuthFlashBling == '__main__':
    app.run(debug=True)

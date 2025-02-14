from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder='public')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/tags')
def get_tags():
    try:
        with open('tags.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            tags = [{'tag': line.split(',')[0].strip(), 'id': line.split(',')[1].strip()} for line in lines if line.strip()]
        return jsonify(tags)
    except Exception as e:
        return jsonify({'error': 'Impossible de lire le fichier des tags.'}), 500

if __name__ == '__main__':
    app.run(port=3000)

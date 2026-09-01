from flask import Flask, send_from_directory
import os

app = Flask(__name__)
CARTELLA = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def elenco():
    file_pdf = [f for f in os.listdir(CARTELLA) if f.lower().endswith('.pdf')]
    righe = ''.join(f'<li><a href="/doc/{f}">{f}</a></li>' for f in file_pdf)
    html = f"""
    <html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body style="font-family: sans-serif; padding: 20px;">
      <h2>Documenti Cantiere</h2>
      <ul>{righe}</ul>
    </body>
    </html>
    """
    return html


@app.route('/doc/<nome>')
def apri(nome):
    return send_from_directory(CARTELLA, nome)


if __name__ == '__main__':
    porta = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=porta)

from flask import Flask, send_from_directory
import os

app = Flask(__name__)
CARTELLA = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def elenco():
    file_pdf = sorted(f for f in os.listdir(CARTELLA) if f.lower().endswith('.pdf'))

    righe = ''.join(
        f'''
        <li class="doc-item">
            <a href="/doc/{f}" target="_blank">
                <span class="icon">📄</span>
                <span class="nome">{f}</span>
                <span class="freccia">›</span>
            </a>
        </li>
        '''
        for f in file_pdf
    )

    html = f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Canale Group - Documenti Cantiere</title>
        <style>
            * {{ box-sizing: border-box; margin: 0; padding: 0; }}
            body {{
                font-family: -apple-system, 'Segoe UI', Roboto, sans-serif;
                background: #f4f6f8;
                color: #1a1a1a;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 24px 16px;
            }}
            .card {{
                background: #ffffff;
                width: 100%;
                max-width: 480px;
                border-radius: 16px;
                box-shadow: 0 2px 16px rgba(0,0,0,0.08);
                overflow: hidden;
            }}
            .header {{
                background: linear-gradient(135deg, #2b2b2f, #48484f);
                color: white;
                padding: 28px 24px;
            }}
            .brand {{
                font-size: 20px;
                font-weight: 700;
                letter-spacing: 1px;
                text-transform: uppercase;
            }}
            .brand .group {{
                font-size: 11px;
                font-weight: 400;
                letter-spacing: 2px;
                opacity: 0.7;
                margin-left: 6px;
            }}
            .badge {{
                font-size: 12px;
                text-transform: uppercase;
                letter-spacing: 1px;
                opacity: 0.85;
                margin-top: 14px;
            }}
            .header h1 {{
                font-size: 22px;
                margin-top: 6px;
                font-weight: 600;
            }}
            .header p {{
                font-size: 13px;
                opacity: 0.9;
                margin-top: 4px;
            }}
            ul {{
                list-style: none;
            }}
            .doc-item a {{
                display: flex;
                align-items: center;
                padding: 16px 20px;
                text-decoration: none;
                color: #1a1a1a;
                border-bottom: 1px solid #eef0f2;
                transition: background 0.15s;
            }}
            .doc-item:last-child a {{
                border-bottom: none;
            }}
            .doc-item a:active,
            .doc-item a:hover {{
                background: #f0f7fc;
            }}
            .icon {{
                font-size: 20px;
                margin-right: 12px;
            }}
            .nome {{
                flex: 1;
                font-size: 15px;
                font-weight: 500;
                word-break: break-word;
            }}
            .freccia {{
                color: #2b2b2f;
                font-size: 20px;
                margin-left: 8px;
            }}
            .footer {{
                text-align: center;
                font-size: 12px;
                color: #8a939c;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="header">
                <div class="brand">CANALE<span class="group">GROUP</span></div>
                <div class="badge">Sicurezza Cantiere</div>
                <h1>Documenti Aggiornati</h1>
                <p>Consultazione documenti per il controllo in cantiere</p>
            </div>
            <ul>
                {righe}
            </ul>
        </div>
        <div class="footer">Aggiornato automaticamente ad ogni modifica</div>
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

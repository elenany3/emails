from flask import Flask, render_template, request
import random

app = Flask(__name__)

# قائمة الدومينات
domains = ['viajemail.com', 'postacasa.com', 'kuchenmail.com', 'boscomail.com']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name'].replace(" ", "").lower()
    
    suggestions = []
    domain_count = len(domains)

    for i in range(20):
        random_number = random.randint(10000, 99999)
        domain = domains[i % domain_count] 
        email = f"{name}{random_number}@{domain}"
        suggestions.append(email)
    
    return render_template('index.html', suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)

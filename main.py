from flask import Flask, render_template, request, jsonify
import secrets
print(secrets.token_hex(24))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_name', methods=['POST'])
def submit_name():
    user_name = request.form.get('userName')
    if user_name:
        return jsonify({'message': f"Happy Birthday {user_name}!", 'status': 'success'})
    else:
        return jsonify({'message': 'Please enter your name!', 'status': 'error'})

@app.route('/submit_gift', methods=['POST'])
def submit_gift():
    gift = request.form.get('gift')
    if gift:
        return jsonify({'message': f'You will receive your gift of "{gift}" shortly!', 'status': 'success'})
    else:
        return jsonify({'message': 'Please enter a gift idea.', 'status': 'error'})

@app.route('/choose_gift', methods=['POST'])
def choose_gift():
    choice = request.form.get('choice')
    if choice == 'yes':
        return jsonify({'message': 'Please enter your gift idea.', 'status': 'success'})
    else:
        return jsonify({'message': "Sorry, you can't select 'No' as I want to gift you something! Please select 'Yes'.", 'status': 'error'})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, session, request, redirect, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fkuywegffkufbf8ywerwp'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():
    # how to get form data is different for GET vs. POST
    if request.method == 'GET':
        first_name = request.args.get('first_name')
        if first_name:
            return render_template('form-demo.html', first_name=first_name)
        else:
            first_name = session.get('first_name')
        return render_template('form-demo.html', first_name=first_name)
    if request.method == 'POST':
        session['first_name'] = request.form['first_name']
        return redirect(url_for('form_demo'))


@app.route('/user/<string:name>/')
def get_user(name):
    return render_template('user.html', user_name=name)


@app.route('/songs')
def get_all_songs():
    songs = [
        'song 1',
        'song 2',
        'song 3'
    ]
    return render_template('songs.html', songs=songs)


if __name__ == '__main__':
        app.run()

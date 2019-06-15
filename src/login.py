import random

from flask import Flask, request, abort, redirect, Response, url_for
from flask_login import LoginManager, login_required, UserMixin, login_user
import questions as q

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, username, password, id, active=True):
        self.id = id
        self.username = username
        self.password = password
        self.active = active

    def get_id(self):
        return self.id

    def is_active(self):
        return self.active

    def get_auth_token(self):
        return make_secure_token(self.username, key='secret_key')


class UsersRepository:

    def __init__(self):
        self.users = dict()
        self.users_id_dict = dict()
        self.identifier = 0

    def save_user(self, user):
        self.users_id_dict.setdefault(user.id, user)
        self.users.setdefault(user.username, user)

    def get_user(self, username):
        return self.users.get(username)

    def get_user_by_id(self, userid):
        return self.users_id_dict.get(userid)

    def next_index(self):
        self.identifier += 1
        return self.identifier


users_repository = UsersRepository()


@app.route('/submit', methods=['GET', 'POST'])
@login_required
def submit():
    choice = request.args.get('choice')
    if not choice:
        return 'You failed to pick anything.... -_-'

    return 'You chose {}'.format(choice)


@app.route('/')
def index():
    return "<h2>Hello PAUL</h2>"

@app.route('/home')
@login_required
def home():
    question = random.choice(q.questions)
    
    htmL = '''
    <form action =/submit>
        <div>
            {}
            <button type="submit" class="btn btn-default">Submit</button>
        </div>
    </form>'''.format(question.ask())

    return htmL


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        registeredUser = users_repository.get_user(username)
        print('Users ' + str(users_repository.users))
        print('Register user %s , password %s' % (registeredUser.username, registeredUser.password))
        if registeredUser != None and registeredUser.password == password:
            print('Logged in..')
            login_user(registeredUser)
            return redirect(url_for('home'))
        else:
            return abort(401)
    else:
        return Response('''
            <form action="" method="post">
                <p><input type=text name=username>
                <p><input type=password name=password>
                <p><input type=submit value=Login>
            </form>
        ''')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username, password, users_repository.next_index())
        users_repository.save_user(new_user)
        return Response("Registered Successfully")
    else:
        return Response('''
            <form action="" method="post">
            <p><input type=text name=username placeholder="Enter username">
            <p><input type=password name=password placeholder="Enter password">
            <p><input type=submit value=Login>
            </form>
        ''')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return users_repository.get_user_by_id(userid)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)

import db
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    html =['<ul>']

    for username, user in db.users.items():

        html.append(
            f"<li><a href='/user/{username}'>{user['name']}</a></li>'"
        )
    html.append('</ul>')
    return '\n'.join(html)
    
app.run()
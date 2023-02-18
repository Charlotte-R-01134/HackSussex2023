from app import create_app, db
from app.models import User

app = create_app()

@app.before_first_request
def before_first_request():
    db.create_all()
    db.session.commit()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)
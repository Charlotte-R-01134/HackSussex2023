from app import create_app, db
from app.models import User, Notes
from flask_login import current_user

app = create_app()

@app.before_first_request
def before_first_request():
    db.create_all()
    db.session.commit()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)


@app.context_processor
def inject_recent():
    if current_user.is_authenticated:
        recent = Notes.query.filter_by(user_id=current_user.id).all()
        # order by last modified
        recent.sort(key=lambda x: x.last_modified, reverse=True)
        # get first 10 notes
        recent = recent[:10]
        return dict(recent=recent)
    return dict(recent=None)
from . import main
from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from .. import db
from ..models import User, Notes
from .forms import NewNoteForm, NoteForm
from datetime import datetime
import markdown

@main.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', current_user=current_user)
    return render_template('index.html', current_user=current_user)

@main.route('/<username>')
def notes(username):
    if current_user.username != username:
        flash('You do not have access to these notes')
        return redirect(url_for('main.index'))
    notes = Notes.query.filter_by(user_id=current_user.id).all()
    # sort alphabetically
    notes.sort(key=lambda x: x.title)
    return render_template('allnotes.html', notes=notes, current_user=current_user)

@main.route('/<username>/notes/<id>/delete')

@main.route('/<username>/notes/<id>/display')
def display(id, username):
    if current_user.username != username:
        flash('You do not have access to these notes')
        return redirect(url_for('main.index'))
    note = Notes.query.filter_by(id=id).first()
    note.content = markdown.markdown(note.content, extensions=['markdown.extensions.fenced_code'])
    note.content = note.content.replace('\n', '<br>')
    note.content = note.content.replace('<script>', '<nice-try>')
    note.content = note.content.replace('<\script>', '')
    return render_template('display.html', note=note, current_user=current_user)

@main.route('/<username>/notes/new-note', methods=['GET', 'POST'])
@login_required
def new_note(username):
    if current_user.username != username:
        flash('You do not have access to these notes')
        return redirect(url_for('main.index'))
    form = NewNoteForm()
    if form.validate_on_submit():
        note = Notes(title=form.title.data, user_id=current_user.id, last_modified=datetime.utcnow())
        db.session.add(note)
        db.session.commit()
        flash('Note created')
        return redirect(url_for('main.get_note', id=note.id, username=username))
    return render_template('new_note.html', id=id, current_user=current_user, form=form)

@main.route('/<username>/notes/<id>', methods=['GET', 'POST'])
@login_required
def get_note(id, username):
    if current_user.username != username:
        flash('You do not have access to these notes')
        return redirect(url_for('main.index'))
    form = NoteForm()
    note = Notes.query.filter_by(id=id).first()
    if form.validate_on_submit():
        note.title = form.title.data
        note.content = form.content.data
        note.last_modified = datetime.utcnow()
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('main.get_note', id=id, username=username))
    form.title.data = note.title
    form.content.data = note.content
    return render_template('notes.html', note=note, form=form)

@main.route('/<username>/notes/<title>/delete')
@login_required
def delete(id, username, title):
    pass
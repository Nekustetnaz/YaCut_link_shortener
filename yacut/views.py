import random
from string import ascii_letters, digits

from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import URLForm
from .models import URLMap

LENGTH = 6


def get_unique_short_id(symbols=ascii_letters + digits, k=LENGTH):
    while True:
        short_id = ''.join(random.choices(symbols, k=k))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        short = custom_id if custom_id else get_unique_short_id()
        url_map = URLMap(
            original=form.original_link.data,
            short=short
        )
        db.session.add(url_map)
        db.session.commit()
        flash(url_for('short_url', short=short, _external=True))
    return render_template('main.html', form=form)


@app.route('/<string:short>')
def short_url(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original)

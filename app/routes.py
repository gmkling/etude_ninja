from app import app
from etude_engine.db import sodb, sodb_music
from app.forms import CompositionResults, LoginForm, SodbMusicForm, SodbListCompositionsForm
from flask import render_template, flash, request, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/compositions', methods=['GET', 'POST'])
def composition():
    form = SodbMusicForm()

    if form.validate_on_submit():
        # On submission, we should do any checking and then pass data on the sodb
        #if db_instance is None:
        db_instance = sodb.Sodb()
        new_record = sodb_music.sodb_music(
            composer='{}'.format(form.composer.data),
            title='{}'.format(form.title.data),
            opus_num=form.opus_num.data,
            date=form.date.data,
            notation_filename='{}'.format(form.notation_filename.data),
            instrumentation='{}'.format(form.instrumentation.data)
        )
        db_instance.add_object(new_record)
        db_instance.commit_changes()
        # on success, flash and redirect to index
        flash('Added {} by {} to composition database...'.format(
            form.title.data, form.composer.data))
        flash('Composition Title: {}'.format(form.title.data))
        flash('Composer: {}'.format(form.composer.data))

        return redirect(url_for('index'))
    return render_template('sodb_music.html', title='Compositions Database', form=form)


@app.route('/edit_composition/<int:id>', methods=['GET', 'POST'])
def edit(id):
    comp_obj = sodb_music.sodb_music()
    comp_obj.id_music = id
    db_obj = sodb.Sodb()
    qry = db_obj.search_compositions(comp_obj)
    record = qry.first()

    if record:
        form = SodbMusicForm(formdata=request.form, obj=record)
        if request.method == 'POST' and form.validate():
            # save edits by looking up by id and adding info, committing
            db_obj.update_entry(record)
            flash('Album updated successfully!')
            return redirect('/')
        return render_template('edit_composition.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)

@app.route('/list_compositions', methods=['GET', 'POST'])
def list_compositions():
    form = SodbListCompositionsForm()
    results = []

    if form.validate_on_submit():
        # On submission, we should do any checking and then pass data on the sodb
        db_instance = sodb.Sodb()
        search_criteria = sodb_music.sodb_music(
            composer='{}'.format(form.composer.data),
            title='%{}%'.format(form.title.data),
            opus_num=form.opus_num.data,
            date=form.date.data,
            notation_filename='%{}%'.format(form.notation_filename.data),
            instrumentation='%{}%'.format(form.instrumentation.data)
        )
        results = db_instance.search_compositions(search_criteria).all()

        if not results:
            flash('No results found!')
            return redirect(url_for('list_compositions', title='Compositions Search', table=None, form=form))
        else:
            table = CompositionResults(results)
            table.border = True
            return render_template('list_compositions.html', title='Compositions Search', table=table, form=form)

    return render_template('list_compositions.html', title='Compositions Search', table=None, form=form)

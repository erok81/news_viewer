from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from scrape import get_paragraphs

app = Flask(__name__)

# Flask-WTF required secret key
app.config['SECRET_KEY'] = 'XXX'
# TODO move this to venv


class GetUrlForm(FlaskForm):
    url = StringField('Enter news site to bypass ads', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = GetUrlForm(request.form)
    if form.validate_on_submit():

        url = form.url.data
        p = get_paragraphs(url)

        if p == 'error':
            flash('Site might be down. Check URL and try again')
            
            return redirect('/')

        return render_template('results.html', p=p)


    return render_template('home.html', form=form)



if __name__ == '__main__':
    app.run(debug=False)
    
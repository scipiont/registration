
from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db, User
from forms import RegistrationForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Регистрация прошла успешно!', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
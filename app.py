from flask import Flask, render_template, redirect, url_for, request
from models import db, JobApplication
from forms import JobForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)
csrf = CSRFProtect(app)

# Home Page - Display & Add Jobs


@app.route('/', methods=['GET', 'POST'])
def index():
    form = JobForm()
    if form.validate_on_submit():
        new_job = JobApplication(
            company=form.company.data,
            role=form.role.data,
            status=form.status.data
        )
        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for('index'))

    jobs = JobApplication.query.all()
    return render_template('index.html', form=form, jobs=jobs)

# Edit job routes


@app.route('/edit/<int:job_id>', methods=['GET', 'POST'])
def edit_job(job_id):
    job = JobApplication.query.get_or_404(job_id)
    form = JobForm(obj=job)

    if form.validate_on_submit():
        job.company = form.company.data
        job.role = form.role.data
        job.status = form.status.data
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', form=form, job=job)

# Delete Job Route


@app.route('/delete/<int:job_id>', methods=['POST'])
@app.route('/delete/<int:job_id>', methods=['POST', 'DELETE'])
def delete_job(job_id):
    job = JobApplication.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return '', 204


if __name__ == '__main__':
    app.run(debug=False)

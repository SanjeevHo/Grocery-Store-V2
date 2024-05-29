from flask import Flask
from flask_security import SQLAlchemySessionUserDatastore , Security
from application.models import db, User , Role
from config import DevelopmentConfig
from application.resources import api
from application.sec import datastore
from application.worker import celery_init_app
import flask_excel as excel
from celery.schedules import crontab
from application.task import daily_reminder,report
from application.instances import cache

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app) # here we are telling our app that we are using sqlalchemy
    api.init_app(app)
    excel.init_excel(app)
    app.security =Security(app,datastore)
    cache.init_app(app)
    with app.app_context():
        import application.views # here we imported the view.py as application context
    return app
app = create_app()
celery_app = celery_init_app(app)

@celery_app.on_after_configure.connect
def send_email(sender,**kwargs):
    sender.add_periodic_task(
        crontab(hour=17,minute=4,day_of_month=25),
        report.s("sanjeevy62358@gmail.com","DailyTest"),  
    )

@celery_app.on_after_configure.connect
def send_daily_reminder(sender,**kwargs):
    sender.add_periodic_task(
        crontab (hour=17,minute=2),
        daily_reminder.s("Admin@email.com","Daily Remainder"),
    )

if __name__ == "__main__":
    app.run(debug=True)  



# celery -A main:celery_app worker -l INFO
# celery -A main:celery_app beat -l INFO
#  ~/go/bin/MailHog
#  redis-server
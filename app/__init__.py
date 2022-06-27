from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)
print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    return render_template('index.html', title="TyRoyLog Portfolio", url=os.getenv("URL"))

@app.route('/tylerswork/')
def tylerwork():
    return render_template('tylerwork.html')
    
@app.route('/tylershobbies/')
def tylerhobby():
    return render_template('tylerhobby.html')

@app.route('/loganswork/')
def loganwork():
    return render_template('loganwork.html')

@app.route('/loganshobbies/')
def loganhobby():
    return render_template('loganhobby.html')

@app.route('/royswork/')
def roywork():
    return render_template('roywork.html')

@app.route('/royshobbies/')
def royhobby():
    return render_template('royhobby.html')

@app.route('/aboutus/')
def aboutus():
    return render_template('aboutus.html')

@app.route('/timeline/')
def timeline():
    posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return render_template('timeline.html', posts=posts)

if __name__ ==  "__main__":
    app.run()

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in
TimelinePost.select().order_by(TimelinePost.created_at.desc()) 
        ]
    
    }

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_post():
    delete_timeline_posts = TimelinePost.delete().execute()
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in
TimelinePost.select().order_by(TimelinePost.created_at.desc()) 
        ]
    }
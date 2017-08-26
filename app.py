from flask import Flask
import mongoengine as me

app = Flask(__name__)

me.connect('mongoengine_test', host='mongodb://mongo', port=27017)

import datetime

class Post(me.Document):
    title = me.StringField(required=True, max_length=200)
    content = me.StringField(required=True)
    author = me.StringField(required=True, max_length=50)
    published = me.DateTimeField(default=datetime.datetime.now)

post_1 = Post(
    title='Sample Post',
    content='Some engaging content',
    author='Scott'
)
post_1.save()       # This will perform an insert
#print(post_1.title)
#post_1.title = 'A Better Post Title'
#post_1.save()       # This will perform an atomic edit on "title"
#print(post_1.title)


@app.route('/')
def hello():
  #return 'Hello, from Docker!'
  ans = ''
  for post in Post.objects:
    ans += post.title
    ans += '\n'

  return ans

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

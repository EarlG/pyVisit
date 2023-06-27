from flask import Flask, render_template
import json

app = Flask(__name__)


def load_photos():
    with open('photos.json', 'r') as file:
        photos = json.load(file)
    return photos


photos = load_photos()


@app.route('/')
def index():
    return render_template('index.html', photos=photos)


@app.route('/<category>')
def show_category(category):
    if category == 'about':
        return render_template('index.html', photos=photos)
    else:
        filtered_photos = [photo for photo in photos if photo['category'] == category]
        return render_template('index.html', photos=filtered_photos)


if __name__ == '__main__':
    app.run()

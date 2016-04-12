from flask import Flask
from flask import render_template
import corpusMetadata as corp
from music21 import corpus
from music21 import converter
# from music21 import LilypondConverter
import os

app = Flask(__name__)

@app.route("/")
def showComposers():
    composers = []
    composerDirs = os.listdir('/Users/TGriffey/anaconda/envs/music21-remix/lib/python2.7/site-packages/music21/corpus')
    for composerDir in composerDirs :
        works = corpus.getComposer(composerDir)
        if len(works) > 0 :
            composers.append(composerDir)
    return render_template('home.html', composers=composers)

@app.route('/composers/<composername>')
def show_composer_works(composername):
    works = []
    workPaths = corpus.getComposer(composername)
    for work in workPaths :
        filenameArr = os.path.split(work)
        works.append({'filename': filenameArr[-1], 'path': work})
    return render_template('composer.html', works=works, composername=composername)

@app.route('/composers/<composername>/<workpath>')
def show_work(composername, workpath):
    stream = converter.parse('/Users/TGriffey/anaconda/lib/python2.7/site-packages/music21-2.2.1-py2.7.egg/music21/corpus/bach/bwv66.6.mxl')
    # file = stream.write('test.png')
    return render_template('work.html', filename=workpath)

if __name__ == "__main__":
    app.debug = True
    app.run()
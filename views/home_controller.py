from flask import render_template
from config import app


class HomeController(object):

    @staticmethod
    @app.route('/')
    def index():
        """metod dlya zagryzki shablona glavnoi sranici"""
        return render_template('home/index.html')

    @staticmethod
    @app.route('/about')
    def about():
        """metod dlya zagryzki shablona sranici pro sait"""
        return render_template('home/about.html')

    @staticmethod
    @app.route('/contact')
    def contact():
        """metod dlya zagryzki shablona sranici contactov"""
        return render_template('home/contact.html')

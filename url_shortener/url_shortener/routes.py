from flask import Blueprint, render_template, request, redirect
from .extensions import db 
from .models import Link
  
from .auth import require_auth
  
shortener = Blueprint('shortener', __name__)

@shortener.route('/<short_url>')
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    link.views = link.views + 1
    db.session.commit()
    return redirect(link.original_url)

@shortener.route('/create_link', methods=['POST'])
def create_link():
    original_url= request.form['original_url']
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()

    return render_template('link_success.html',
        new_url=link.short_url, original_url=link.original_url)

@shortener.route('/')
def index():
    return render_template('index.html')

@shortener.route('/analytics')
@require_auth
def analytics():
    links = Link.query.all()
  
    return render_template('analytics.html', links=links)

@shortener.errorhandler(404)
def page_not_found(e):
    return '<h1>Page_Not_Found 404</h1>', 404



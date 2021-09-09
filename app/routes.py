from flask import Flask, Blueprint, request, render_template, url_for

path = Blueprint(
                        'path', __name__,
                        url_prefix='/',
                        template_folder="templates"
                    )

bp = Blueprint('errors', __name__)

@bp.app_errorhandler(404)
def handle_404(err):
    return render_template('404.html'), 404

@path.route('/', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@path.route('/news', methods=['GET', 'POST'])
def news():
    return render_template('news.html')

# @path.route('/test', methods=['GET', 'POST'])
# def test():
#     return render_template('index.html')
# @path.errorhandler(404)
# def not_found_error(e):
#     return render_template('404.html'), 404

# @path.errorhandler(404)
# def handle_bad_request(e):
#     return 'bad request!', 404
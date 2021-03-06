from flask import Flask, Blueprint, request, render_template, url_for

path = Blueprint(
                        'path', __name__,
                        url_prefix='/',
                        template_folder="templates"
                    )

@path.route('/', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

# @path.route('/manual', methods=['GET', 'POST'])
# def manual():
#     return render_template('manual.html')

@path.app_errorhandler(404) # 'errorhandler' not working cause of blueprint usage, only 'app_errorhandler'
def not_found_error(e):
    return render_template('404.html'), 404

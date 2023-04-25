from flask import Flask, render_template
import traceback
def create_app():
    app = Flask(__name__)
    
    app.secret_key = 'some_secret'
    @app.errorhandler(TypeError)
    def handle_type_error(e):
        traceback.print_exc()
        return render_template('index.html'), 500
    
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
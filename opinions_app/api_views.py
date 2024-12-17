# what_to_watch/opinions_app/api_views.py

# Импортируем метод jsonify:
from flask import jsonify

from . import app
from .models import Opinion


# Явно разрешаем метод GET:
@app.route('/api/opinions/<int:id>/', methods=['GET'])
def get_opinion(id):
    # Получаем объект по id или выбрасываем ошибку 404:
    opinion = Opinion.query.get_or_404(id)
    # Конвертируем данные в JSON и возвращаем JSON-объект и HTTP-код ответа:
    return jsonify({'opinion': opinion}), 200

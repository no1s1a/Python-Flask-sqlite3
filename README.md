Для создания проекта с использованием Python, Flask, авторизацией, регистрацией и базой данных SQLite, следуйте указанным ниже шагам.

1. Установите Flask и другие необходимые библиотеки
2. Создайте новую папку проекта и в ней файл app.py
3. Создайте файлы шаблонов login.html, register.html и index.html в папке templates
4. Создайте файл base.html в папке templates
5. Запустите app.py, и он создаст базу данных SQLite и запустит сервер.
6. Теперь вы можете добавить, удалить и редактировать данные, создав маршруты и функции для каждого из этих действий. Пример маршрута для добавления данных:
@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        NN = request.form['NN']
        NAME = request.form['NAME']
        mFreeMB = request.form['mFreeMB']
        # ... добавьте остальные данные здесь
        UserZ = current_user.username
        new_zamer = Zamer(NN=NN, NAME=NAME, mFreeMB=mFreeMB, UserZ=UserZ)
        db.session.add(new_zamer)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')
        
7. Создайте файл шаблона add.html в папке templates
8. Добавьте маршруты и функции для удаления и редактирования данных по аналогии с добавлением данных. Например, для удаления данных:
@app.route('/delete/<int:id>')
@login_required
def delete(id):
    zamer = Zamer.query.get_or_404(id)
    db.session.delete(zamer)
    db.session.commit()
    return redirect(url_for('index'))
    9. Для редактирования данных создайте маршрут и функцию edit:

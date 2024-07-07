# test_investera


**Создайте простой API блога с помощью. API должен иметь следующие конечные точки:

1. [X] GET /posts: Возвращает список всех сообщений блога.
2. [X] GET /posts/{id}: Возвращает одну запись блога по идентификатору.
3. [X] POST /posts: Создать новую запись в блоге.
4. [X] PUT /posts/{id}: Обновить существующую запись в блоге.
5. [X] DELETE /posts/{id}: Удалить запись в блоге.

Каждая запись в блоге должна иметь следующие поля:

1. [X] id (integer, primary key)
2. [X] title (string)
3. [X] content (string)
4. [X] created_at (datetime)
5. [X] updated_at (datetime)

Требования:

* [X] Для создания API используйте любой фреймворк, который посчитаете оптимальным.
* [ ] Используйте базу данных Postgres.
* [X] Используйте JSON в качестве формата ответа.

** Бонусные очки:**

* [X] Реализуйте пагинацию для GET /posts.
* [X] Добавьте GET /posts/search, позволяющую искать записи в блоге по названию или содержанию.
* [X] Оберните в docker.

Практические результаты:

* [X] Репозиторий Git, содержащий код.
* [ ] Файл README с инструкциями по запуску.
* [ ] Краткий отчет, поясняющий проектные решения и любые проблемы, возникшие в ходе реализации.

Примечание:

* Вы можете использовать любые дополнительные библиотеки или инструменты, которые, по вашему мнению, необходимы для выполнения задачи.
* Если вы не уверены в какой-либо части задания, вы можете задавать уточняющие вопросы.
* Пожалуйста, отправьте свое решение в виде репозитория Git и убедитесь, что оно общедоступно.

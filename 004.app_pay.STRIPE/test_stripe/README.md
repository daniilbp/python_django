Запуск ПО:

1. В settings.py папки пр-та (test_stripe) ввести STRIPE_PUBLIC_KEY и STRIPE_SECRET_KEY от вашей Stripe dashboard, своей тестовой среды, где у вас есть нужные ключи. Вам понадобится ваш public key и secret key. Если у вас их нет, создайте их сейчас. Скопируйте эти значения и перенесите их в файл настроек Django: 

    # Stripe

    STRIPE_PUBLIC_KEY = "pk_test_1234"
    STRIPE_SECRET_KEY = "sk_test_1234"

2. Запустите программу в терминале выполнив:

    -> cd <путь к проекту>
    -> python3 manage.py runserver

3. Создать суперпользователя: python3 manage.py createsuperuser (например: Admin/Admin без почты)

4. По адресу http://127.0.0.1:8000/admin/ входим в Django Admin панель используя логин/пароль от суперюзера.

5. Создаем продукт(ы) во вкладке - PRODUCTS / Items нажав Add

6. В браузере переходите по адресу: http://127.0.0.1:8000/ и попадаете на Главную страницу чернового варианта проекта.

7. Переходим по ссылкам...

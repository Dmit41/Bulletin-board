# Bulletin-board

Чтобы токен работал корректно нужно в админ панели домен поменять на http://127.0.0.1:8000

CKeditor не позволит пользователям добавлять картинки и видео, пока по адресу /venv/lib/python3.10/site-packages/ckeditor_uploader/urls.py не заменить адреса на:

    re_path(r'^upload/', login_required(views.upload), name='ckeditor_upload'),
    re_path(r'^browse/', never_cache(login_required(views.browse)), name='ckeditor_browse'),
 Естествено добавив from django.contrib.auth.decorators import login_required   
 

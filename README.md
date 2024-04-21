# template_api

- 設定項目

docker-compose.yaml
```
environment:
      - MYSQL_ROOT_PASSWORD=root
      - MYSQL_DATABASE=<リポジトリ名>←ここを変更する。
```

djangoのプロジェクト作成コマンド
```
django-admin startproject --template=custom_project_teamplte config
```
djangoのカスタムユーザ作成コマンド
```
django-admin startapp --template=custom_user_template user
```
djangoの新規アップ作成コマンド
```
django-admin startapp --template=custom_app_template myapp
```

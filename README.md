# traq-statistics-server
## dev environment
- use DevContainer with VSCode
- set up powerlevel10k
- set up conda by `conda init zsh`
- create conda env by `conda env create --file env.yaml`
- activate conda env by `conda activate traq-statistics-server`
- download unidic by `python -m unidic download`
- start up mariadb by `sudo service mariadb start`
- set up mariadb by `sudo mysql_secure_installation`
    - root password: `root`
- add user to mariadb
    - login to mariadb `mariadb -u root -p`
    - create user by `create user 'test'@'localhost' identified by 'password';`
    - create database by `create database test;`
    - add access rights to user by `GRANT ALL PRIVILEGES ON test.* TO test@localhost IDENTIFIED BY 'password';`
    - logout by `quit`
- add traQ token by `export TRAQ_ACCESS_TOKEN=hogehogepunipuni`

## development
### create app
- `python manage.py startapp polls`
- add views to `view.py`

### add or update models
- `cd mysite`
- `python manage.py makemigrations main`
- `python manage.py migrate`

### run devserver
- `cd mysite`
- `python manage.py runserver`

### shell
- `python manage.py shell`

## statistics
### user
- 指定期間(1日～全期間)の
  - [x] 時間・曜日別の投稿頻度
  - [x] 累計投稿数の推移
  - [x] メッセージランキング
    - [x] スタンプをつけた人数
    - [x] スタンプの種類別(1人1つとカウント)
  - [ ] ワードマップ
  - [x] つけたスタンプの統計

### word

## others
- api: https://apis.trap.jp

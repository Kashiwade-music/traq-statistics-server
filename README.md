# traq-statistics-server
## dev environment
- use DevContainer with VSCode
- set up powerlevel10k
- set up conda by `conda init zsh`
- create conda env by `conda env create --file env.yaml`
- activate conda env by `conda activate traq-statistics-server`
- start up mariadb by `sudo service mariadb start`
- set up mariadb by `sudo mysql_secure_installation`
    - root password: `root`
- add user to mariadb
    - login to mariadb `mariadb -u root -p`
    - create user by `create user 'test'@'localhost' identified by 'password';`
    - create database by `create database test;`
    - add access rights to user by `GRANT ALL PRIVILEGES ON test.* TO test@localhost IDENTIFIED BY 'password';`
    - logout by `quit`
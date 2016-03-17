from fabric.api import *
from fabric.contrib import django
from fabvenv import virtualenv
from fabric.colors import green, cyan, red, blue


django.project('open_gates')

env.user = 'ubuntu'
env.key_filename = "~/.ssh/id_rsa"

DB = {
    'database': 'open_gates',
    'username': '<user>',
    'password': '<pass>'
}


def live():
    global PATH, ENV_PATH, ENV_NAME, BRANCH
    env.hosts = ["<host_ip>"]
    ENV_NAME = red('LIVE')
    PATH = '/var/www/html/open_gates'
    ENV_PATH = '/var/www/env'
    BRANCH = 'master'


def deploy():
    print(blue(" -------------- "))
    print(cyan("Deploying on {0}".format(ENV_NAME)))
    print(blue(" -------------- "))

    with cd(PATH), virtualenv(ENV_PATH):
        run('git pull --no-edit origin ' + BRANCH)
        run('pip install -r requirements.txt')
        rmanage('migrate')
        clean()
        print(green("-------------"))
        print(green("Deploy done"))
        print(green("-------------"))


def rmanage(command):
    with cd(PATH), virtualenv(ENV_PATH):
        run("./manage.py {0}".format(command))


def clean():
    with cd(PATH):
        run('find . -name "*.pyc" -delete')


# INSTALLATION ON A NEW MACHINE
def install():
    "Clone git repo into PATH. The %username% branch will be checked out."
    if exists(PATH):
        print("Folder {0} already exists !".format(PATH))
    else:
        run('git clone -b {0} {1} {2}'.format(env.user, REPO, PATH))
    create_db()
    run('pip install -r requirements.txt')
    rmanage('migrate')
    clean()
    print(green("-------------"))
    print(green("Installation done"))
    print(green("-------------"))


def create_db():
    "Create database"
    run("mysql -u {username} -p {password} -e 'CREATE SCHEMA '{database}'\
        DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci'".format(**DB))

from fabric.api import env, task, run
from fabric.context_managers import prefix

env.use_ssh_config=True

env.hosts = ['medmed']
gunicorn_pid = 'gunicorn_pid'
port=8001
appenv='appenv'


def activate():
    return 'cd {0} && source bin/activate'.format(appenv)

@task
def start():
    with prefix(activate()):
        print "Starting the app"
        run('gunicorn --daemon -p {0} -b 0.0.0.0:{1} app:app'.format(gunicorn_pid, port))

@task
def stop():
    with prefix(activate()):
        print "Stopping the app"
        run('kill -9 `cat {0}`'.format(gunicorn_pid))
        run('rm {0}'.format(gunicorn_pid))

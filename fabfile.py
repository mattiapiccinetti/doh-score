from fabric.api import env, task, run
from fabric.context_managers import prefix

env.use_ssh_config=True

env.hosts = ['medmed']
gunicorn_pid = 'gunicorn_pid'
port=8001

contexts = {
    'mattia': {
        'port': 8001,
        'virtualenv': 'appenv'
    },
    'ari': {
        'port': 8002,
        'virtualenv': 'appenv'
    }
}

def activate(context_name):
    return 'cd {0} && source bin/activate'.format(context_name)


def get_context(context_name):
    if not context_name in contexts:
        abort("No context named {0}".format(context_name))
    return contexts[context_name] 

@task
def start(context_name):
    context = get_context(context_name)
    with prefix(activate(context['virtualenv'])):
        print "Starting the app on context ".format(context_name)
        run('gunicorn --daemon -p {0} -b 0.0.0.0:{1} app:app'.format(gunicorn_pid, port))

@task
def stop(context_name):
    context = get_context(context_name)
    with prefix(activate(context['virtualenv'])):
        print "Stopping the app on context ".format(context_name)
        run('kill -9 `cat {0}`'.format(gunicorn_pid))
        run('rm {0}'.format(gunicorn_pid))

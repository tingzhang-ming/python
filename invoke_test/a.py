from invoke import task


@task
def t1(ctx, docs=False):
    ctx.run('ls')


@task
def build(ctx, docs=False):
    ctx.run("python setup.py build")
    if docs:
        ctx.run("sphinx-build docs docs/_build")


if __name__ == '__main__':
    t1()

#!/usr/bin/env python
import os
import tempfile
import subprocess
from urlparse import urljoin

github_user = "mhcvs2"
github_password = ""

gitee_user = "mhcvs"
gitee_password = ""

gitlab_user = "hongchao.ma@samsung.com"
gitlab_password = "qq77aa88"

git_auth_file = os.path.join(os.path.expanduser('~'), '.git-credentials')

pull_config = [
    {
        "url": "https://github.com",
        "repo": "mhcvs2",
        "projects": [
            "cpp",
            "prometheusExporter"
        ]
    }
]

push_config = {
    "url": "https://gitee.com",
    "repo": "mhcvs",
    "project": "save"
}


def get_project_url(url, repo, project):
    return urljoin(urljoin(url, repo), '{}.git'.format(project))


def run_shell(cmd):
    subprocess.check_output(args=cmd, shell=True)


def clone_and_rmgit(url, repo, project):
    run_shell("git clone {}".format(get_project_url(url, repo, project)))
    os.rmdir(os.path.join(project, '.git'))


def push(url, repo, project):
    run_shell("git repo add origin {}".format(get_project_url(url, repo, project)))
    run_shell("git add --all")
    run_shell('git commit -m"first"')
    run_shell('git push origin master')


def git_auth():
    run_shell('git config --global credential.helper store')
    with open(git_auth_file, 'w') as f:
        lines = []
        if gitee_user:
            lines.append('https://{}:{}@gitee.com'.format(gitee_user, gitee_password))
        if github_user:
            lines.append('https://{}:{}@github.com'.format(github_user, github_password))
        if gitlab_user:
            lines.append('http://{}:{}@gitlab.gcloud.srcb.com'.format(gitlab_user, gitlab_password))
        f.writelines(lines)


def clear(work_dir):
    if os.path.exists(git_auth_file):
        os.remove(git_auth_file)
    if work_dir and os.path.isdir(work_dir):
        os.rmdir(work_dir)


def main():
    work_dir = None
    try:
        work_dir = tempfile.mkdtemp()
        print "work dir: ", work_dir
        os.chdir(work_dir)
        git_auth()
        for pc in pull_config:
            for p in pc['project']:
                clone_and_rmgit(pc['url'], pc['repo'], p)
        push(push_config['url'], push_config['repo'], push_config['project'])
    except Exception as e:
        print "error: "
        print e.message
    finally:
        clear(work_dir)


if __name__ == '__main__':
    main()

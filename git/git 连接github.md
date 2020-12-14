正常情况下，你项目下面的 .git 目录config文件，如果像下面这样，就能连接你的gihub。

这些小节，都是通过git命令生成的。
```
[core]
        repositoryformatversion = 0
        filemode = false
        bare = false
        logallrefupdates = true
        symlinks = false
        ignorecase = true
[user]
        name = liuning800203
        email = liuning800203@gmail.com
[remote "origin"]
        url = git@github.com:WallaceLiu/baobaotao-web.git
        fetch = +refs/heads/*:refs/remotes/origin/*
```

- 配置本机的git
```
$ git config --global user.name "liuning800203"
$ git config --global user.email liuning800203@gmail.com
```
- 生成密钥
```
$ ssh-keygen -t rsa -C "liuning800203@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/cap/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/cap/.ssh/id_rsa.
Your public key has been saved in /Users/cap/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:Sz57mIh+7tUogRA5UWSRWZ4sR77HapybGvDnpMYM/mo liuning800203@gmail.com
The key's randomart image is:
+---[RSA 2048]----+
……
+----[SHA256]-----+
```
- 提交密钥

查看密钥：
```
$ less /Users/cap/.ssh/id_rsa.pub
```
把密钥复制到github。登录github在setting->SSH and GPG keys->SSH keys中，将上面密钥复制进去。
- 检验是否连接github
```
$ ssh git@github.com
The authenticity of host 'github.com (192.30.255.112)' can't be established.
RSA key fingerprint is SHA256:…….
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.255.112' (RSA) to the list of known hosts.
PTY allocation request failed on channel 0
Hi WallaceLiu! You've successfully authenticated, but GitHub does not provide shell access.
Connection to github.com closed.
$ ssh git@github.com
You've successfully authenticated, but GitHub does not provide shell access.
```
说明成功。
- 本地项目
假设，你将来想创建一个叫baobaotao-web项目。
```
$ mkdir baobaotao-web
$ cd baobaotao-web/
```
初始化这个目录：
```
$ git init
Initialized empty Git repository in /Users/cap/git/baobaotao-web/.git/
```
> 否则会出现“Initialized empty Git repository in /Users/cap/git/.git/”

再生成一个README文件：
```
$ touch README
```
随便编辑README这个文件：
```
$ vim README
```
查看本地文件变化：
```
$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	README

nothing added to commit but untracked files present (use "git add" to track)
```
看到变化了吧，这几步都是git操作，如果你忘了，就复习一下。

剩下的，把这些变化提交到github上。
```
$ git add .
$ git commit -am '初始提交'
[master (root-commit) ec173cc] 初始提交
 1 file changed, 1 insertion(+)
 create mode 100644 README
```
把远程Git更名为origin：
```
$ git remote add origin git@github.com:WallaceLiu/baobaotao-web.git
& git remote set-url origin git@github.com:WallaceLiu/baobaotao-web.git
```
推送到远端：
```
$ git push -u origin master
```

上面我没成功。

实在不行，直接在github上创建一个。然后 git clone 下载到本地。
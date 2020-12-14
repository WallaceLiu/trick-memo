**使用 git add 添加需要追踪的新文件和待提交的更改， 然后使用 git status 和 git diff 查看有何改动， 最后用 git commit 将你的快照记录。这就是你要用的基本流程，绝大部分时候都是这样的。**

# git add 添加文件到缓存
**在提交你修改的文件之前，你需要把它们添加到缓存。**

如果该文件是新创建的，执行 git add 将该文件添加到缓存，即便该文件已经被 add，只要修改了也要add。让我们看几个例子：

回到我们的 Hello World 示例，初始化该项目之后，我们就要用 git add 将我们的文件添加进去了。 我们可以用 git status 看看我们的项目的当前状态。
```
$ git status -s
?? README
?? hello.rb
```
"?"表示尚未被追踪（未添加到缓存）的文件。现在添加。
```
$ git add README hello.rb
```
再执行 git status：
```
$ git status -s
A  README
A  hello.rb
```
此时这俩文件已经加到缓存了，标记变成“A”。

新项目中，添加所有文件很普遍，可以在当前工作目录执行命令：
```
git add .
```
递归地执行命令时所在的目录中的所有文件。此时，git add . 就和 git add README hello.rb 效果一样。

此外，效果一致的还有 git add *，不过那只是因为我们这还没有子目录，不需要递归而已。

再跑执行 git status，有点古怪。
```
$ vim README
$ git status -s
AM README
A  hello.rb
```
“AM” 状态是，这个文件在我们将它添加到缓存之后又有改动。因此，如果我们现在提交快照，记录的将是上次执行 git add 时的文件版本，而不是现在在磁盘中的这个。

Git 并不认为磁盘中的文件与你想快照的文件必须是一致的 —— （如果你需要它们一致，）得用 git add 命令告诉它。

**当你要将你的修改包含在即将提交的快照里的时候，执行 git add。 任何你没有添加的改动都不会被包含在内 —— 这意味着你可以比绝大多数其他源代码版本控制系统更精确地归置你的快照。**

> 查看《Pro Git》中 git add 的 “-p” 参数，以了解更多关于提交文件的灵活性的例子。

# git status 查看你的文件在工作目录与缓存的状态
执行 git status 查看你的代码在缓存与当前工作目录的状态。

加 -s 参数，可以获得简短的结果。否则，将告诉你更多的提示与上下文信息。
```
$ git status -s
AM README
A  hello.rb
```
```
$ git status
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
# new file:   README
# new file:   hello.rb
#
# Changed but not updated:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
# modified:   README
#
```
**简短的输出看起来很紧凑。而详细输出则很有帮助。** Git 还会告诉你在你上次提交之后，有哪些文件被删除、修改或者存入缓存了。
```
$ git status -s
M  README
 D hello.rb
```
**简短输出中有两栏。第一栏是缓存的，第二栏是工作目录的。**

所以假设你临时提交了 README 文件，然后又改了，并且没有执行 git add，你会看到如下信息：
```
$ git status -s
MM README
 D hello.rb
```
**执行 git status 以查看在你上次提交之后有啥被修改或者临时提交了， 从而决定自己是否需要提交一次快照，同时也能知道有什么改变被记录进去了。**

# git diff 显示已写入缓存与已修改但尚未写入缓存的改动的区别
git diff 有两个主要的应用场景。我们将在此介绍其一， 在 检阅与对照 一章中，我们将介绍其二。

我们这里介绍的方式是用此命令描述已临时提交的或者已修改但尚未提交的改动。

> - 尚未缓存的改动，显示自从上次提交快照后，尚未缓存的所有更改
> - 查看已缓存的改动，显示接下来要写入快照的内容
> - 查看已缓存的与未缓存的所有改动，显示工作目录与上一次提交的更新的区别，无视缓存

### git diff 尚未缓存的改动
无参数，会以规范化的 diff 格式显示自从上次提交快照之后尚未缓存的所有更改。
```
$ vim hello.rb
$ git status -s
 M hello.rb
$ git diff
diff --git a/hello.rb b/hello.rb
index d62ac43..8d15d50 100644
--- a/hello.rb
+++ b/hello.rb
@@ -1,7 +1,7 @@
 class HelloWorld

   def self.hello
-    puts "hello world"
+    puts "hola mundo"
   end

 end
```
所以，git status显示你上次提交更新至后所更改或者写入缓存的改动， 而 git diff 一行一行地显示这些改动具体是啥。

**通常执行完 git status 之后接着跑一下 git diff 是个好习惯。**

### git diff --cached 查看已缓存的改动
会告诉你有哪些内容已经写入缓存了。也就是说，显示接下来要写入快照的内容。

所以，如果你将上述示例中的 hello.rb 写入缓存，因为 git diff 显示的是尚未缓存的改动，所以在此执行它不会显示任何信息。
```
$ git status -s
 M hello.rb
$ git add hello.rb 
$ git status -s
M  hello.rb
$ git diff
$ 
```
如果你想看看已缓存的改动，你需要执行的是 git diff --cached。
```
$ git status -s
M  hello.rb
$ git diff
$ 
$ git diff --cached
diff --git a/hello.rb b/hello.rb
index d62ac43..8d15d50 100644
--- a/hello.rb
+++ b/hello.rb
@@ -1,7 +1,7 @@
 class HelloWorld

   def self.hello
-    puts "hello world"
+    puts "hola mundo"
   end

 end
```
### git diff HEAD 查看已缓存的与未缓存的所有改动
一并查看已缓存的与未缓存的改动，也就是说，你要看到的是工作目录与上一次提交的更新的区别，无视缓存。

假设又改了 ruby.rb，那缓存的与未缓存的改动我们就都有了。

以上三个 diff 命令的结果如下：
```
$ vim hello.rb 
$ git diff
diff --git a/hello.rb b/hello.rb
index 4f40006..2ae9ba4 100644
--- a/hello.rb
+++ b/hello.rb
@@ -1,7 +1,7 @@
 class HelloWorld

+  # says hello
   def self.hello
     puts "hola mundo"
   end

 end
$ git diff --cached
diff --git a/hello.rb b/hello.rb
index 2aabb6e..4f40006 100644
--- a/hello.rb
+++ b/hello.rb
@@ -1,7 +1,7 @@
 class HelloWorld

   def self.hello
-    puts "hello world"
+    puts "hola mundo"
   end

 end
$ git diff HEAD
diff --git a/hello.rb b/hello.rb
index 2aabb6e..2ae9ba4 100644
--- a/hello.rb
+++ b/hello.rb
@@ -1,7 +1,8 @@
 class HelloWorld

+  # says hello
   def self.hello
-    puts "hello world"
+    puts "hola mundo"
   end

 end
```
### git diff --stat 显示摘要而非整个 diff
如果我们不想要看整个 diff 输出，但是又想比 git status 详细点， 就可以用 --stat 选项。该选项使它显示摘要而非全文。

上文示例在使用 --stat 选项时，输出如下：
```
$ git status -s
MM hello.rb
$ git diff --stat
 hello.rb |    1 +
 1 files changed, 1 insertions(+), 0 deletions(-)
$ git diff --cached --stat
 hello.rb |    2 +-
 1 files changed, 1 insertions(+), 1 deletions(-)
$ git diff HEAD --stat
 hello.rb |    3 ++-
 1 files changed, 2 insertions(+), 1 deletions(-)
```
你还可以在上述命令后面制定一个目录，从而只查看特定文件或子目录的 diff 输出。

**执行 git diff 来查看 git status 执行的详细结果信息 —— 一行一行地显示这些文件是如何被修改或写入缓存的。**

# git commit 记录缓存内容的快照
现在已经用 git add 将想要快照的内容写入了缓存，再执行 git commit 就将它实际存储快照了。 

Git 为你的每一个提交都记录你的名字与电子邮箱地址，所以第一步是告诉 Git 这些都是啥。
```
$ git config --global user.name 'Your Name'
$ git config --global user.email you@somedomain.com
```
现在，写入缓存，并提交对 hello.rb 的所有改动。使用 -m 选项以在命令行中提供提交注释。
```
$ git add hello.rb 
$ git status -s
M  hello.rb
$ git commit -m 'my hola mundo changes'
[master 68aa034] my hola mundo changes
 1 files changed, 2 insertions(+), 1 deletions(-)
```
现在我们已经记录了快照。如果我们再执行 git status，会看到我们有一个“干净的工作目录”。 这意味着我们在最近一次提交之后，没有做任何改动 —— 在我们的项目中没有未快照的工作。
```
$ git status
# On branch master
nothing to commit (working directory clean)
```
如果漏掉 -m 选项，Git 会尝试为你打开一个编辑器以填写提交信息。 
如果 Git 在你对它的配置中找不到相关信息，默认会打开 vim。屏幕会像这样：

通常，撰写良好的提交信息是很重要的。不成文的规定：

简短的关于改动的总结（25个字或者更少）

如果有必要，更详细的解释文字。约 36 字时换行。在某些情况下，
第一行会被作为电子邮件的开头，而剩余的则会作为邮件内容。
将小结从内容隔开的空行是至关重要的（除非你没有内容）；
如果这两个待在一起，有些 git 工具会犯迷糊。

空行之后是更多的段落。

 - 列表也可以

 - 通常使用连字符（-）或者星号（*）来标记列表，前面有个空格，
   在列表项之间有空行，不过这些约定也会有些变化。
```
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
# modified:   hello.rb
#
~
~
~
".git/COMMIT_EDITMSG" 25L, 884C written
```
提交注解是很重要的。因为 Git 很大一部分能耐就是它在组织本地提交和与他人分享的弹性， 它很给力地能够让你为逻辑独立的改变写三到四条提交注解，以便你的工作被同仁审阅。因为提交与推送改动是有区别的， 请务必花时间将各个逻辑独立的改动放到另外一个提交，并附上一份良好的提交注解， 以使与你合作的人能够方便地了解你所做的，以及你为何要这么做。

git commit -a 自动将在提交前将已记录、修改的文件放入缓存区
如果你觉得 git add 提交缓存的流程太过繁琐，Git 也允许你用 -a 选项跳过这一步。 基本上这句话的意思就是，为任何已有记录的文件执行 git add —— 也就是说，任何在你最近的提交中已经存在，并且之后被修改的文件。 这让你能够用更 Subversion 方式的流程，修改些文件，然后想要快照所有所做的改动的时候执行 git commit -a。 不过你仍然需要执行 git add 来添加新文件，就像 Subversion 一样。
```
$ vim hello.rb
$ git status -s
 M  hello.rb
$ git commit -m 'changes to hello file'
# On branch master
# Changed but not updated:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
# modified:   hello.rb
#
no changes added to commit (use "git add" and/or "git commit -a")
$ git commit -am 'changes to hello file'
[master 78b2670] changes to hello file
 1 files changed, 2 insertions(+), 1 deletions(-)
```
注意，如果你不缓存改动，直接执行 git commit，Git 会直接给出 git status 命令的输出，提醒你啥也没缓存。我已将该消息中的重要部分高亮，它说没有添加需要提交的缓存。 如果你使用 -a，它会缓存并提交每个改动（不含新文件）。

现在你就完成了整个快照的流程 ——改些文件，然后用 git add 将要提交的改动提交到缓存， 用 git status 和 git diff 看看你都改了啥，最后 git commit 永久地保存快照。

简而言之，执行 git commit 记录缓存区的快照。如果需要的话，这个快照可以用来做比较、共享以及恢复。

# git reset HEAD 取消缓存已缓存的内容
git reset 可能是人类写的最费解的命令了。 我用 Git 有些年头了，甚至还写了本书，但有的时候还是会搞不清它会做什么。 所以，我只说三个明确的，通常有用的调用。请你跟我一样尽管用它 —— 因为它可以很有用。

在此例中，我们可以用它来将不小心缓存的东东取消缓存。假设你修改了两个文件，想要将它们记录到两个不同的提交中去。 你应该缓存并提交一个，再缓存并提交另外一个。如果你不小心两个都缓存了，那要如何才能取消缓存呢？ 你可以用 git reset HEAD -- file。 技术上说，在这里你不需要使用 -- —— 它用来告诉 Git 这时你已经不再列选项，剩下的是文件路径了。 不过养成使用它分隔选项与路径的习惯很重要，即使在你可能并不需要的时候。

好，让我们看看取消缓存是什么样子的。这里我们有两个最近提交之后又有所改动的文件。我们将两个都缓存，并取消缓存其中一个。
```
$ git status -s
 M README
 M hello.rb
$ git add .
$ git status -s
M  README
M  hello.rb
$ git reset HEAD -- hello.rb 
Unstaged changes after reset:
M hello.rb
$ git status -s
M  README
 M hello.rb
```
现在你执行 git commit 将只记录 README 文件的改动，并不含现在并不在缓存中的 hello.rb。

如果你好奇，它实际的操作是将该文件在“索引”中的校验和重置为最近一次提交中的值。 git add 会计算一个文件的校验和，将它添加到“索引”中， 而 git reset HEAD 将它改写回原先的，从而取消缓存操作。

如果你想直接执行 git unstage，你可以在 Git 中配置个别名。 执行 git config --global alias.unstage "reset HEAD" 即可。 一旦执行完它，你就可以直接用 git unstage [file] 作为代替了。

如果你忘了取消缓存的命令，Git 的常规 git status 输出的提示会很有帮助。 例如，在你有已缓存的文件时，如果你不带 -s 执行 git status，它将告诉你怎样取消缓存：
```
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#   modified:   README
#   modified:   hello.rb
#
```
**执行 git reset HEAD 以取消之前 git add 添加，但不希望包含在下一提交快照中的缓存。**

# git rm 将文件从缓存区移除
git rm 会将条目从缓存区中移除。这与 git reset HEAD 将条目取消缓存是有区别的。 “取消缓存”的意思就是将缓存区恢复为我们做出修改之前的样子。 在另一方面，git rm 则将该文件彻底从缓存区踢出，因此它不再下一个提交快照之内，进而有效地删除它。

默认情况下，git rm file 会将文件从缓存区和你的硬盘中（工作目录）删除。 如果要在工作目录中留着该文件，可以使用 git rm --cached

git mv git rm --cached orig; mv orig new; git add new

不像绝大多数其他版本控制系统，Git 并不记录记录文件重命名。它反而只记录快照，并对比快照以找到有啥文件可能被重命名了。 如果一个文件从更新中删除了，而在下次快照中新添加的另一个文件的内容与它很相似，Git 就知道这极有可能是个重命名。 因此，虽然有 git mv 命令，但它有点多余 —— 它做得所有事情就是 git rm --cached， 重命名磁盘上的文件，然后再执行 git add 把新文件添加到缓存区。 你并不需要用它，不过如果觉得这样容易些，尽管用吧。

**我自己并不使用此命令的普通形式 —— 删除文件。通常直接从硬盘删除文件，然后执行 git commit -a 会简单些。 它会自动将删除的文件从索引中移除。**

**执行 git rm 来删除 Git 追踪的文件。它还会删除你的工作目录中的相应文件。**
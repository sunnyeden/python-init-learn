#### git版本控制器

* 世界上最先进的分布式版本控制系统

* 版本控制/分布式是git的两大特点

#### mac中安装git

`sudo apt-get install git`

#### 创建版本控制器

`git init` 初始化仓库

`git add ./`

`git commit -m"备注"`

`git log` 查看创建的版本

#### 版本回退

`git reset --hard 版本号`

#### 查看历史操作记录，进行回退到指定版本

`git log --pretty=oneline`

`git reflog`

`git reset --hard 版本号[31dc7d4]`

#### 撤销修改

`git checkout -- [文件名]`

#### 对比文件不同

`git diff -- HEAD [文件名]`

#### 删除文件

`git rm [文件]`

`git commit -m"备注"`

#### 查看分支

`git branch`

#### 创建分支并切换

`git chekout -b dev`

#### 合并分支

`git checkout master`

`git merge dev`

#### 删除分支

`git branch -d dev`

#### 查看分支图

`git log --graph --pretty=oneline`

#### 分支管理策略，禁止快速合并模式

`git merge --no-ff dev -m"禁止fast-forward"`

#### bug修复模式案例

* 比如你开发了一半，此时线上有bug产生需要立马修复，但是你的工作空间又不能提交上去

`git checkout -b dev`

* 保存开发现场

`git stash`

* 切换到主分支上创建新的分支修复bug

`git checkout -b bug`

* 解决完后合并bug分支，并删除bug分支

`git merge --no-ff bug -m"修复bug"`

`git checkout -d bug`

* 切换到dev分支，解锁现场，继续工作

`git stash list`

`git stash pop`
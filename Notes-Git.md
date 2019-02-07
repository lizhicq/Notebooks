## 跳回特定commit
$ git reset --hard abcd

## 遇到大文件
$git lfs install

## Resolve Conflict
$git show # adjust then
$git add .

## hard reset to remote
$git fetch origin
$git reset --hard origin/master

## if you want to save your local 

$git commit -a -m "Saving my work, just in case"
$git branch my-saved-work

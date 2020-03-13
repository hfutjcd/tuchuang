自己做的一个简单图床

1.github上创建一个仓库作为图床。

2.本地创建一个仓库，通过 git remote add origin git@github.com:\xxxxx.git 添加远程仓库。


3.修改upload的repourl地址为你的远程仓库 url。

4. 在typora的 '偏好设置->图像->上传服务' 选择 '自定义' ,自定义命令填  'python path/to/upload.py'

5. 点击'验证图片上传项' 测试是否成功。

6. 在文档中右键图片选择上传。
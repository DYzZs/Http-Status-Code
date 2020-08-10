# Usage:
* * * *
  1. 建议在`python`3.6以上运行

  2. 安装第三方包：

     `pip3 install -r requirements.txt`

  3. 将收集子域名保存在xxx.txt文件中运行

     `python3 http_status_codes.py xxx.txt`

  4. 注意: 如果fake_useragent发生如下错误：

     ```
     fake_useragent.errors.FakeUserAgentError: Maximum amount of retries reached
     ```

     请执行 `python3 -c "import tempfile;print(tempfile.gettempdir())"` 获取当前系统的缓存目录

     然后使用 `wget https://fake-useragent.herokuapp.com/browsers/0.1.11 -O fake_useragent_0.1.11.json`

     将json文件下下来, 再移动到刚刚得到的缓存目录下.

環境 : Centos 7 且有裝 Python3.6

1. 將 google.repo 放到 /etc/yum.repos.d/ 下
2. 執行 yum update
3. 執行 yum install google-chrome-stable -y
4. 將 chromedriver.exe 放到 /usr/local/share/chromedriver 下 (也可放到其他地方 但需更改py檔中的路徑
5. 執行 pip3 install selenium
6. 執行 python3.6 apple_download.py
7. 執行完過10秒左右完後會產生新的output.csv 每次執行完會覆蓋掉舊的csv檔

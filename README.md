mybox
====

* Static Info:
  ![Bash使用](https://img.shields.io/badge/Bash_Script-2A2Ba2)
  ![Docker使用](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
  ![Python使用](https://img.shields.io/badge/Python-14354C.svg?logo=python&logoColor=white)
* Development:
  ![版權宣告](https://img.shields.io/badge/license-MIT-brightgreen)


# 1. 功能簡介
- 提供一組Docker相關腳本，運行腳本後可建立簡單紅隊靶機，作為示範教學使用。
- 靶機漏洞：HTTP非加密的連線、弱密碼和SUID提權

# 2. 項目介紹

## 2.1. Release Asset

- **data資料夾**：配合dockerfile設定所需檔案
- **dockerfile檔案**：容器創建文件
- **LICENSE檔案**：版權宣告
- **README.md檔案**：說明文件

# 3. 作業運用

## 3.1 Repo構管

* 此Repo為public，設定保護main branch。
* 主要更新於develop branch執行後，pull request回main branch。

## 3.2. 模組設計

* 於README.md及/doc/design.vpp說明。
* 主要規格為：
  * 可組建靶機容器映像檔
  * 靶機具備外部滲透弱點：HTTP非加密的連線、弱密碼
  * 靶機具備內部提權弱點：linux SUID提權

## 3.3. 模組發展

### 3.3.1. 使用說明

將最新release下載並解壓縮後，依序於本機執行以下命令：
```
docker build -t vulnerable-ubuntu .
docker run -d -p 2222:22 -p 8080:80 --name vulnerable-container vulnerable-ubuntu
```

### 3.3.2. 模組發佈

* 檢核後手動發佈

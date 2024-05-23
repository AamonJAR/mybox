# 基於 Ubuntu 20.04 的基礎映像建立 Docker 容器
FROM ubuntu:20.04

# 安裝所需的軟件包和庫
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        openssh-server \
        apache2 \
        sudo \
        python3 \
        python3-pip \
        netcat \
        dos2unix \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 安裝 Python 庫
RUN pip3 install paramiko pytest

# 複製本地腳本到容器內
COPY boxInitialize.sh /root/boxInitialize.sh
COPY test.py /root/test.py

# 轉換腳本格式以避免潛在問題
RUN dos2unix /root/boxInitialize.sh

# 賦予腳本執行權限並運行
RUN chmod +x /root/boxInitialize.sh
RUN /root/boxInitialize.sh

# 曝露必要端口
EXPOSE 22 80 4444

# 設定容器啟動命令以啟動 SSH 和 HTTP 服務
CMD service ssh start && service apache2 start && tail -f /dev/null

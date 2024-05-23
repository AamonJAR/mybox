#!/bin/bash

# 靶機管理設定
echo ""
echo "靶機管理設定"
# 新增使用者
if ! id "boxadmin" > /dev/null 2>&1; then
    useradd -m boxadmin
    usermod -aG root boxadmin
    echo "boxadmin:GJ1FWcRKG86XbNb4Njhk" | chpasswd
fi

# 檢查 SSH 服務是否存在，若不存在，則安裝
if ! systemctl is-active --quiet ssh; then
    apt-get update
    apt-get install -y openssh-server
    service ssh start
fi

# 檢查 HTTP 服務是否存在，若不存在，則安裝
if ! systemctl is-active --quiet apache2; then
    apt-get update
    apt-get install -y apache2
    service apache2 start
fi

# 外部滲透設定
echo ""
echo "外部滲透設定"
# 新增外部測試使用者 charlie
if ! id "charlie" > /dev/null 2>&1; then
    useradd -m charlie
    echo "charlie:aPjWy5wKMmHKrpRr1qm4" | chpasswd
fi

# 利用 HTTP 服務藏一個封包中含有以下帳號密碼資訊
echo "username: charlie password: aPjWy5wKMmHKrpRr1qm4" > /var/www/html/credentials.txt

# 創建測試文件
echo "user's flag" > /home/charlie/user.txt
chown charlie:charlie /home/charlie/user.txt

# 重新啟動 SSH 服務
service ssh restart

# 內部提權設定
echo ""
echo "內部提權設定"
# 檢查 sudo 是否存在，若不存在，則安裝
if ! command -v sudo > /dev/null 2>&1; then
    apt-get update
    apt-get install -y sudo
fi

# 設定 SUID 權限旗標到 /bin/bash 執行檔上
chmod u+s /bin/bash

# 創建 root 的旗標文件
echo "root's flag" > /root/root.txt
chown root:root /root/root.txt
chmod 600 /root/root.txt

# 完成設定
echo ""
echo "完成設定"

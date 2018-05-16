# coding=utf-8
import paramiko
import time


class SSHRelatedHelper(object):

    def __init__(self, host_name, user, password):
        self.client = paramiko.SSHClient()  # define the ssh client
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # allow to connect the server which is not in know_hosts file
        self.host_name = host_name
        self.user = user
        self.password = password

    def is_ssh_success(self):
        try:
            self.client.connect(hostname=self.hostname, port=22, username=self.username, password=self.password, timeout=4)
            return True
        except Exception, e:
            return e

    def excute_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command, timeout=20)
        return stdin, stdout, stderr

    def is_download_file_by_wget_successfully(self, download_url, downloaded_file_name):
        wget_command = 'wget --no-proxy ' + download_url
        stdin, stdout, stderr = self.excute_command(wget_command)
        downloaded_success = False
        # for line in stderr:
        #     if "'+" + downloaded_file_name + "'" + "saved" in line:
        #         downloaded_success = True
        #         break
        find_downloaded_file_command = 'find / -name "*%s*"' % downloaded_file_name
        stdin2, stdout2, stderr2 = self.excute_command(find_downloaded_file_command)
        for line in stdout2.readlines():
            if downloaded_file_name in line:
                downloaded_success = True
        return downloaded_success

    def is_file_already_existed(self, file_name):
        existed_already = False
        find_file_command = 'find / -name "*%s*"' % file_name
        stdin, stdout, stderr = self.excute_command(find_file_command)
        for line in stdout.readlines():
            if file_name in line:
                existed_already = True
                break
        return existed_already

    def install_sw_by_rpm_or_deb(self, file_name):
        if '.rpm' in file_name:
            install_sw_command = 'sudo rpm -ihv ' + file_name
        elif '.deb' in file_name:
            install_sw_command = 'sudo dpkg -i ' + file_name
        self.excute_command(install_sw_command)

    def is_install_sw_by_rpm_or_deb_successful(self, file_name):
        installed_successfully = False
        installed_package = file_name.split(".")[0]
        if '.rpm' in file_name:
            check_if_installed_command = 'sudo rpm -qa | grep ' + installed_package
        elif '.deb' in file_name:
            check_if_installed_command = 'sudo dpkg -l | grep  ' + installed_package
        stdin, stdout, stderr = self.excute_command(check_if_installed_command)
        for line in stdout.readlines():
            if installed_package in line:
                installed_successfully = True
                break
        return installed_successfully










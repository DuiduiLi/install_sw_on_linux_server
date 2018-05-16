# coding=utf-8
from djangoautoconf.cmd_handler_base.msg_process_cmd_base import DjangoCmdBase
from install_sw_on_linux_server.management.command.base_util.ssh_related_helper import SSHRelatedHelper


class SoftwareInstaller(DjangoCmdBase):
    host_name = ''   # server IP
    user = ''    # login username
    password = ''   # login password
    download_url = ''    # the url address which used to download file, like 'http://xx.xx.xx.xx/Debian/Labadmin.3.1.3.0.Debian.x64.deb'
    downloaded_file_name = ''   #  the downloaded file name, it should be included in downloaded_url also, like 'Labadmin.3.1.3.0.Debian.x64.deb'

    def msg_loop(self):
        ssh_helper = SSHRelatedHelper(self.host_name, self.user, self.password)
        is_ssh_login_success = ssh_helper.is_ssh_success()
        if is_ssh_login_success:
            if not ssh_helper.is_file_already_existed(self.downloaded_file_name):
                if ssh_helper.is_download_file_by_wget_successfully(self.download_url, self.downloaded_file_name):
                    ssh_helper.install_sw_by_rpm_or_deb(self.downloaded_file_name)
                    if ssh_helper.is_install_sw_by_rpm_or_deb_successful(self.downloaded_file_name):
                        print 'Install SW successfully'
                    else:
                        print 'Failed to install SW by rpm or deb'
                else:
                    print 'Failed to download file by wget'
            else:
                print 'The downloaded file is already existed in server'
        else:
            print 'Failed to log in server by SSH, because ' + unicode(is_ssh_login_success)

Command = SoftwareInstaller


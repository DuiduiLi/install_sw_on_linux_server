# install_sw_on_linux_server

Django framework

It is used to download file by wget, and install downloaded file to server by rpm or deb

first it will check if SSH login is successfully
second it will check if the downloaded file already existed
third it will download file by wget if file is not existed already
fourth it will install downloaded file by rpm or deb
finally it will check if installation is successfully

please provide your server IP, login user name, password, downloaded file url and downloaded file name
then you can use all functions created in base_util/ssh_related_helper.py

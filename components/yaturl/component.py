import batou.component
import batou.lib.python
import batou_ext.git
import batou_ext.ssh


class YatURL(batou.component.Component):

    # This is just a meta class as the service is currently running
    # elsewhere but I need to provide some basic data for Nginx

    running_on = '62.75.244.115'
    port = 80

    def configure(self):
        self.provide('yaturl', self)

        self.mysql = self.require_one('mysql')

        venv = batou.lib.python.VirtualEnv('2.7')
        self += venv
        venv += batou.lib.python.Package('pymysql', version='0.9.3')
        venv += batou.lib.python.Package('sqlalchemy', version='1.2.16')

        self.checkout = batou_ext.git.GitCheckout(
            git_clone_url = 'https://github.com/frlan/yaturl.git',
            git_revision = '1a90a620aa1bd59fae9eb70ffc698d1df570f3a0',
            git_target = self.map('checkout'),
            scan_host = False)

        self += self.checkout

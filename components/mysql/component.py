import batou.component
import batou.lib.mysql


class MySQL(batou.component.Component):

    database = batou.component.Attribute(str, 'yaturl')
    username = None
    password = None
    admin_password = None
    allow_from_hostname = batou.component.Attribute(str, '%')

    def configure(self):
        self.provide('mysql', self)

        self += batou.lib.mysql.Database(
            self.database,
            admin_password=self.admin_password)
        self += batou.lib.mysql.User(
            self.username,
            password=self.password,
            admin_password=self.admin_password,
            allow_from_hostname=self.allow_from_hostname)
        self += batou.lib.mysql.Grant(
            self.database,
            user=self.username,
            admin_password=self.admin_password,
            allow_from_hostname=self.allow_from_hostname)

import batou.component
import batou_ext.mysql


class MySQL(batou.component.Component):

    database = batou.component.Attribute(str, 'yaturl')
    username = None
    password = None
    admin_password = None
    allow_from_hostname = batou.component.Attribute(str, '%')

    def configure(self):
        self += batou_ext.mysql.MySQLGeneric(
            self.database,
            username=self.username,
            password=self.password,
            admin_password=self.admin_password,
            allow_from_hostname=self.allow_from_hostname)

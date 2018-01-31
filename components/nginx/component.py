from batou.lib.cron import CronTab
import batou.component
import batou.lib.file
import batou_ext.nix
import batou_ext.ssl


class CertCheck(batou.component.Component):

    namevar = 'name'

    def configure(self):
        self += batou.lib.nagios.ServiceCheck(
            self.expand(
                'https://{{component.parent.public_name}} certificate valid?'),
            name=self.expand('ssl_cert_{{component.name}}'),
            command='check_http',
            args=self.expand(
                '-H {{component.parent.ssl_address.connect.host}} '
                '-p {{component.parent.ssl_address.connect.port}} '
                '-S --sni -C 14,7'))

@batou_ext.nix.rebuild
class Nginx(batou.component.Component):

    public_name = 'yaturl.net'
    alias = ''

    key_content = None
    crt_content = None
    letsencrypt = batou.component.Attribute('literal', True)
    docroot = None

    def configure(self):
        self.yaturl = self.require_one('yaturl')

        self.address = batou.utils.Address(self.public_name, 80)
        self.ssl_address = batou.utils.Address(self.public_name, 443)

        if not self.docroot:
            self.docroot = self.map('htdocs')
        self += batou.lib.file.File(
            self.docroot,
            ensure='directory',
            leading=True)

        self.cert = batou_ext.ssl.Certificate(
            self.public_name,
            docroot=self.docroot,
            key_content=self.key_content,
            crt_content=self.crt_content,
            use_letsencrypt=self.letsencrypt,
            extracommand='sudo systemctl reload nginx')

        self += self.cert

        self += batou.lib.file.File('yaturl.conf')

 #       self += CertCheck('yaturl')

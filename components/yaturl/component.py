import batou.component

class YatURL(batou.component.Component):

    # This is just a meta class as the service is currently running
    # elsewhere but I need to provide some basic data for Nginx

    host = '62.75.244.115'
    port = 80

    def configure(self):
        self.provide('yaturl', self)

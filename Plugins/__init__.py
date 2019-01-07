import datetime


class Result:
    def __init__(self, ip, port, success=True, info=None):
        """
        Scanner result.
        :param ip: ip of our target.
        :param port: port of the ip.
        :param success: if the plugin get success.
        :param info: the information from plugin.
        """
        self.ip = ip
        self.port = port
        self.info = info
        self.success = success
        self.timestamp = datetime.datetime.now()

    def __repr__(self):
        return "[%s:%s]: %s" % (self.ip, self.port, self.info)

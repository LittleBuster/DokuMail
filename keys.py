class AppKeys():
    """
    Singleton class for loging app
    """

    def new(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance

    def get_config_key(self):
        key = {}
        key["key"] = b"*"
        key["IV"] = b"*"
        return key

    def get_cert_key(self):
        key = {}
        key["key"] = b'*'
        key["IV"] = b'*'
        return key
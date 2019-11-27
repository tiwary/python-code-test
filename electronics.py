class Electronics:
    """Class for Electronics"""

    def __init__(self):
        """Init Server"""
        self.cpu_cores = 8
        self.memory_gb = 8
        self.supported_features = ['Wi-Fi',
                                   'Bluetooth',
                                   'Speakers']

    def is_feature_supported(self, feature_name: str):
        """Check if a provided feature is supported

        :param feature_name: Name of the feature
        :returns boolean  True if feature is supported, False otherwise
        """
        for i in range(len(self.supported_features) - 1):
            if feature_name == self.supported_features[i]:
                return True
        return False


class TV(Electronics):
    """Class for TV"""

    def __init__(self):
        """Init TV"""
        super(TV, self).__init__()
        self.cpu_cores = 1
        self.memory_gb = 2
        self.supported_features.extend(['USB 3.0',
                                        'HDMI',
                                        'Headphone Jack',
                                        'Remote'])


class Laptop(Electronics):
    """Class for Laptop"""

    def __init__(self):
        """Init Laptop"""
        super(Laptop, self).__init__()
        self.cpu_cores = 2
        self.memory_gb = 6
        self.supported_features.extend(['NFC',
                                        'USB-C',
                                        'Touchscreen',
                                        'GPS',
                                        'Accelerometer',
                                        'Fingerprint sensor',
                                        'Phone Calls'])


class Smartphone(Electronics):
    """Class for Smartphone"""

    def __init__(self):
        """Init Smartphone"""
        super(Smartphone, self).__init__()
        self.cpu_cores = 2
        self.memory_gb = 6
        self.supported_features.extend(['Touchscreen',
                                        'Phone Calls',
                                        'Data Network'])

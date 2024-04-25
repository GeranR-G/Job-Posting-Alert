import configparser
from os.path import exists

class ConfigSetting:

    def __init__(self):
        config_path = "config.ini"
        Config = configparser.ConfigParser()
        if not exists(config_path):
            GenerateConfig(Config, config_path)
        Config.read(config_path)
        self.your_gmail = ConfigSectionMap(Config, "User Data")["yourgmail"]
        self.email_list = ConfigSectionMap(Config, "User Data")["emaillist"]
        self.email_list = self.email_list.split(",")
        self.file_path = ConfigSectionMap(Config, "User Data")["filepath"]
        self.alert_days = Config.getint("Date Data", "alertdays")
        self.snapshot_days = Config.getint("Date Data", "snapshotdays")

def GenerateConfig(Config, config_path):
    cfgfile = open(config_path, "w")
    Config.add_section("User Data")
    Config.add_section("Date Data")
    Config.set("User Data", "YourGmail", "")
    Config.set("User Data", "EmailList", "")
    Config.set("User Data", "FilePath", "")
    Config.set("Date Data", "AlertDays", "5")
    Config.set("Date Data", "SnapshotDays", "30")
    Config.write(cfgfile)
    cfgfile.close()    

def ConfigSectionMap(Config, section):
    dict = {}
    options = Config.options(section)
    for option in options:
        try:
            dict[option] = Config.get(section, option)
            if dict[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict[option] = None
    return dict
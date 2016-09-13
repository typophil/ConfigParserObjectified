from sys import version_info
if version_info[0] == 2:
    from ConfigParser import ConfigParser
elif version_info[0] == 3:
    from configparser import ConfigParser

class ConfigObject(object):

    class StandInObject(object):
        """
        As object does not have a __dict__ method, you
        cannot simply add attributes to it
        """
        pass

    def __init__(self, cfg_file):
        PARSER = ConfigParser()
        PARSER.read(cfg_file)

        for cfg_section in PARSER.sections():
            # First round, create objects
            for cfg_option in PARSER.options(cfg_section):
                setattr(self, cfg_section, self.StandInObject())
            # Second round, add attributes
            for cfg_option in PARSER.options(cfg_section):
                # Set the values for the section options
                setattr(getattr(self, cfg_section), cfg_option, PARSER.get(cfg_section, cfg_option))
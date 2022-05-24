import configparser 
config = configparser.ConfigParser() 
config.add_section('postgresql')
config.set('postgresql', 'host','localhost')
config.set('postgresql', 'user','finxter1')
config.set('postgresql', 'port','5543')
config.set('postgresql','password','myfinxterpw')
configfile = open("Write_from_configparser.cfg",'w')
config.write(configfile)
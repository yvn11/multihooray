#!/usr/bin/python
#
# hoorayclient.py
# a multi-thread client with mainloop of dbus-python
#
# Author: Zex <top_zlynch@yahoo.com>
#

from hooraybasic import *

#import signal

class CliHooray(dbus.service.FallbackObject):

  def __init__(self):
    connection = dbus.SessionBus()
    connection_name = dbus.service.BusName(
        HOORAY_CAKE_SUPPERMAN+".Faker", bus = connection)
    dbus.service.Object.__init__(self, connection_name,
        HOORAY_CAKE_SUPPERMAN_DOOR_PATH+"/Faker")

    @dbus.service.method(HOORAY_CAKE_SUPPERMAN_DOOR_RED_IFACE,
            in_signature = '', out_signature = 's',
            path_keyword = 'path')
    def hello(self, path = HOORAY_CAKE_SUPPERMAN_DOOR_PATH+"/Faker"):
        return 'Service unique name: ['+self.connection.get_unique_name()+']'

def client_main(conn, obj, iface):
    
    #print blue_iface
    print obj.Introspect()
    print iface.hello()
    print obj.get_dbus_method('hello',
        HOORAY_CAKE_SUPPERMAN_DOOR_BLUE_IFACE)
    print obj.get_dbus_method('multiply',
        HOORAY_CAKE_FORD_ORION_IFACE)(100, 45)
    print obj.get_dbus_method('emit_signal_with_signature',
        HOORAY_CAKE_FORD_ZEPHYR_IFACE)('open_door', 'red')
    print obj.get_dbus_method('emit_signal_with_signature',
        HOORAY_CAKE_FORD_ZEPHYR_IFACE)('open_door', 'black')
    print obj.get_dbus_method('emit_signal',
        HOORAY_CAKE_SUPPERMAN_DOOR_BLUE_IFACE)('jump_high')
    print obj.get_dbus_method('emit_signal_with_signature',
        HOORAY_CAKE_FORD_ZEPHYR_IFACE)('set_room', 972)

def do_multiply(obj, n0, n1):
     print obj.get_dbus_method('multiply',
        HOORAY_CAKE_FORD_ORION_IFACE)(n0, n1)

def do_quit(iface):
    iface.emit_signal('quit')

def called():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    
    print "CliHooray........"
    obj = CliHooray()
    connection = dbus.StarterBus()

    print "Start CliHooraying........"
    gobject.MainLoop().run()

def calling():

    connection = dbus.SessionBus()
    obj = connection.get_object(HOORAY_CAKE_SUPPERMAN,
        HOORAY_CAKE_SUPPERMAN_DOOR_PATH)

    blue_iface = dbus.Interface(obj,
        HOORAY_CAKE_SUPPERMAN_DOOR_BLUE_IFACE)
    count = 0

    for i in range(7):
#    while( True ):
      sys.stdout.write('[' + str(count) + '] 45 * 100 = ')
      threading.Thread(target = do_multiply,\
            args = (obj, 100, 45)).run()
      count += 1
      time.sleep(2)
"""
def do_when_quit( signo, frame ):
    global loop
    global keep_calling
    
    print "signal[", signo, "]", "Vacation's coming !!..."
    
    loop.quit()
    keep_calling = False
"""
def main():
    gobject.threads_init()
    dbus.glib.init_threads()
    """
    try:
    """
    threading.Thread(target = calling).start()
    threading.Thread(target = called).start()
    print "[All OK]"
    """
    except KeyboardInterrupt, SystemExit:
        loop.quit()
        keep_calling = False
        print "[", time.time(), "]", "Vacation's coming !!..."
    """

if __name__ == '__main__':
    main()

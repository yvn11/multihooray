#!/usr/bin/python
#
# hooray.py
# a simple server of dbus python
# 
# Author: Zex <top_zlynch@yahoo.com>
#

from hooraybasic import *

#dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
#dbus.service.Object.SUPPORTS_MULTIPLE_OBJECT_PATHS = True
#dbus.service.Object.SUPPORTS_MULTIPLE_CONNECTIONS = True

class Hooray(dbus.service.FallbackObject):

  def __init__(self):
    connection = dbus.SessionBus()
    connection_name = dbus.service.BusName(
        HOORAY_CAKE_SUPPERMAN, bus = connection)
    dbus.service.Object.__init__(self, connection_name,
        HOORAY_CAKE_SUPPERMAN_DOOR_PATH)
    self.add_to_connection(connection,
        HOORAY_CAKE_FORD_PATH)
    obj = connection.get_object(
        HOORAY_CAKE_SUPPERMAN,
        HOORAY_CAKE_SUPPERMAN_DOOR_PATH)
    obj.connect_to_signal(
        'open_door', open_door_handler,
        dbus_interface = HOORAY_CAKE_SUPPERMAN_DOOR_BLUE_IFACE)
    obj.connect_to_signal(
        'set_room', set_room_handler,
        dbus_interface = HOORAY_CAKE_FORD_FUSION_IFACE)

    @dbus.service.method(HOORAY_CAKE_SUPPERMAN_DOOR_BLUE_IFACE,
            in_signature = '', out_signature = 's',
            path_keyword = 'path')
    def hello(self, path = HOORAY_CAKE_SUPPERMAN_DOOR_PATH):
        return 'Service unique name: ['+self.connection.get_unique_name()+']'

    @dbus.service.method(HOORAY_CAKE_SUPPERMAN_DOOR_BLUE_IFACE, 
        path_keyword = 'path')
    def emit_signal(self, signal,
        path = HOORAY_CAKE_SUPPERMAN_DOOR_PATH):
        try:
            eval('self.'+signal+'()')
        except Exception as e:
            return 'error on sending signal %s'\
                % (signal)
        return 'signal sent'

    @dbus.service.method(HOORAY_CAKE_FORD_ZEPHYR_IFACE,
        path_keyword = 'path')
    def emit_signal_with_signature(self, signal,
        signature = None,
        path = HOORAY_CAKE_FORD_PATH):
        try:
            if type(signature) is dbus.String:
                eval('self.'+signal+'(\''+signature+'\')')
            else:
                eval('self.'+signal+'('+str(signature)+')')
        except Exception as e:
            return 'error on sending signal %s with signature [%s]'\
                % (signal, signature)
        return 'signal sent with signature'

    @dbus.service.method(HOORAY_CAKE_FORD_ORION_IFACE,
            in_signature = 'ii', out_signature = 'i',
            path_keyword = 'path')
    def multiply(self, n0, n1, path = HOORAY_CAKE_FORD_PATH):
        #return '%d * %d = %d' % (n0, n1, n0 * n1)
        return n0 * n1

    @dbus.service.signal(HOORAY_CAKE_SUPPERMAN_DOOR_BLUE_IFACE,
        signature = 's')
    def open_door(self, color):
        print '%s door is opened' % color

    @dbus.service.signal(HOORAY_CAKE_FORD_FUSION_IFACE)
    def jump_high(self):
        print 'I\'ll jump high'

    @dbus.service.signal(HOORAY_CAKE_FORD_FUSION_IFACE,
        signature = 'i')
    def set_room(self, nroom):
        print 'setting room ...'

    @dbus.service.signal(HOORAY_CAKE_SUPPERMAN_DOOR_BLUE_IFACE)
    def quit(self):
        loop.quit()

def open_door_handler(*args):
    print 'open_door_handler() is working...'
    print 'incoming argument : ', args

def set_room_handler(nroom):
    room = nroom
    print 'current room: %d' % room

def main():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    global loop
    global room

    obj = Hooray()
    loop = gobject.MainLoop()
    '''
      Nevermind, nothing to do with the main loop
    '''
    connection = dbus.StarterBus()
    connection.add_signal_receiver(open_door_handler,
        signal_name = 'jump_high')

    '''
      The main loop goes here
    '''
    print "Hooray is running..."
    loop.run()
    print "Nice weekend, nice beach :D"

if __name__ == '__main__':
    main()

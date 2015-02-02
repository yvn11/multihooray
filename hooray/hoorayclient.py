#!/usr/bin/python

from hooraybasic import *
from dbus.decorators import signal
def wwwooo():
   print "wwwooo"
def client_main(conn, obj, iface):
	
	#print blue_iface
    
    print obj.Introspect()
    """
	print iface.hello()
	print obj.get_dbus_method('hello',
		HOORAY_CAKE_SUPPERMAN_DOOR_BLUE_IFACE)
	print obj.get_dbus_method('multiply',
		HOORAY_CAKE_FORD_ORION_IFACE)(100, 45)
    """
    print obj.get_dbus_method('emit_signal_with_signature',
        HOORAY_CAKE_FORD_ZEPHYR_IFACE)('open_door', 'red')
    """
	print obj.get_dbus_method('emit_signal_with_signature',
		HOORAY_CAKE_FORD_ZEPHYR_IFACE)('open_door', 'black')
	print obj.get_dbus_method('emit_signal',
		HOORAY_CAKE_SUPPERMAN_DOOR_BLUE_IFACE)('jump_high')
	print obj.get_dbus_method('emit_signal_with_signature',
		HOORAY_CAKE_FORD_ZEPHYR_IFACE)('set_room', 972)
    """
#    @dbus.service.signal(HOORAY_CAKE_SUPPERMAN_DOOR_BLUE_IFACE, 's', 'open_door')

def do_multiply(obj, n0, n1):
	 print obj.get_dbus_method('multiply',
		HOORAY_CAKE_FORD_ORION_IFACE)(n0, n1)

def do_quit(iface):
	iface.emit_signal('quit')

def main():

#    	gobject.threads_init()
#	dbus.glib.init_threads()

	connection = dbus.SessionBus()
	obj = connection.get_object(HOORAY_CAKE_SUPPERMAN,
		HOORAY_CAKE_SUPPERMAN_DOOR_PATH)

	blue_iface = dbus.Interface(obj,
		HOORAY_CAKE_SUPPERMAN_DOOR_BLUE_IFACE)
    
#	for i in range(7):
#	 	sys.stdout.write('45 * 100 = ')
#		threading.Thread(target = do_multiply,\
#			args = (obj, 100, 45)).run()
#		time.sleep(1)
    
	client_main(connection, obj, blue_iface)

#	threading.Thread(target = do_quit(blue_iface)).start()

if __name__ == '__main__':
	main()

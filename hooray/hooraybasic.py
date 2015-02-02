#!/usr/bin/python

import dbus
import gobject
import dbus.service
import dbus.mainloop.glib
import threading
import dbus.glib
import time
import sys

HOORAY_CAKE_SUPPERMAN = "hooray.cake.supperman"
HOORAY_CAKE_SUPPERMAN_DOOR_PATH = "/hooray/cake/supperman/door"
HOORAY_CAKE_SUPPERMAN_DOOR_BLUE_IFACE = "hooray.cake.supperman.blue"
HOORAY_CAKE_SUPPERMAN_DOOR_RED_IFACE = "hooray.cake.supperman.red"
HOORAY_CAKE_SUPPERMAN_DOOR_GREEN_IFACE = "hooray.cake.supperman.green"
HOORAY_CAKE_FORD_PATH = "/hooray/cake/ford"
HOORAY_CAKE_FORD_ORION_IFACE = "hooray.cake.orion"
HOORAY_CAKE_FORD_FUSION_IFACE = "hooray.cake.fusion"
HOORAY_CAKE_FORD_ZEPHYR_IFACE = "hooray.cake.zephyr"

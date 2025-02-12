from labgrid.resource.udev import KMTronicRelay
from labgrid.driver.kmtronicrelay import KMTronicRelayDriver
from labgrid.driver.usbloader import UUUDriver
from labgrid.util.managedfile import ManagedFile
from labgrid import Environment
from labgrid.util.helper import get_user
from labgrid.util.ssh import sshmanager
import os

def test_uuu_ManagedFile(target):
    env = Environment('kmtronic.yaml')
    t = env.get_target('main')
    r = t.get_resource("NetworkIMXUSBLoader")
    uuu = t.get_driver("UUUDriver")

    t.activate(uuu)
    uuu.load()

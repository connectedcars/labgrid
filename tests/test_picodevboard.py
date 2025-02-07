from labgrid.resource.udev import PicoDevBoard
from labgrid.driver.picodevboard import PicoDevBoardDriver


def test_picodevboard_resource(target):
    r = PicoDevBoard(target, name=None, match={"ID_SERIAL_SHORT": "e661410403143232"})


def test_picodevboard_driver(target):
    r = PicoDevBoard(target, name=None, match={"ID_SERIAL_SHORT": "e661410403143232"})
    d = PicoDevBoardDriver(target, name=None, cmd="dut_power")
    target.activate(d)


def test_picodevboard_power(target):
    r = PicoDevBoard(target, name=None, match={"ID_SERIAL_SHORT": "e661410403143232"})
    d = PicoDevBoardDriver(target, name=None, cmd="dut_power")
    target.activate(d)
    d.set(1)
    assert d.get() == 1
    d.set(0)
    assert d.get() == 0

def test_picodevboard_ignition(target):
    r = PicoDevBoard(target, name=None, match={"ID_SERIAL_SHORT": "e661410403143232"})
    power = PicoDevBoardDriver(target, name="dut_power", cmd="dut_power")
    target.activate(power)
    power.set(1)
    ignition = PicoDevBoardDriver(target, name="dut_ignition", cmd="dut_ignition")
    target.activate(ignition)
    ignition.set(1)
    assert ignition.get() == 1
    ignition.set(0)
    assert ignition.get() == 0

def test_picodevboard_recovery_mode(target):
    r = PicoDevBoard(target, name=None, match={"ID_SERIAL_SHORT": "e661410403143232"})
    d = PicoDevBoardDriver(target, name=None, cmd="dut_recovery_mode")
    target.activate(d)
    d.set(1)
    assert d.get() == 1
    d.set(0)
    assert d.get() == 0

def test_picodevboard_usb_power(target):
    r = PicoDevBoard(target, name=None, match={"ID_SERIAL_SHORT": "e661410403143232"})
    d = PicoDevBoardDriver(target, name=None, cmd="dut_usb_power")
    target.activate(d)
    d.set(1)
    assert d.get() == 1
    d.set(0)
    assert d.get() == 0

def test_picodevboard_uart_data(target):
    r = PicoDevBoard(target, name=None, match={"ID_SERIAL_SHORT": "e661410403143232"})
    d = PicoDevBoardDriver(target, name=None, cmd="dut_uart_data")
    target.activate(d)
    d.set(1)
    assert d.get() == 1
    d.set(0)
    assert d.get() == 0

def test_picodevboard_uart_power(target):
    r = PicoDevBoard(target, name=None, match={"ID_SERIAL_SHORT": "e661410403143232"})
    d = PicoDevBoardDriver(target, name=None, cmd="dut_uart_power")
    target.activate(d)
    d.set(1)
    assert d.get() == 1
    d.set(0)
    assert d.get() == 0

def test_picodevboard_gpi1(target):
    r = PicoDevBoard(target, name=None, match={"ID_SERIAL_SHORT": "e661410403143232"})
    d = PicoDevBoardDriver(target, name=None, cmd="gpi1")
    target.activate(d)
    d.set(1)
    assert d.get() == 1
    d.set(0)
    assert d.get() == 0

def test_picodevboard_gpi2(target):
    r = PicoDevBoard(target, name=None, match={"ID_SERIAL_SHORT": "e661410403143232"})
    d = PicoDevBoardDriver(target, name=None, cmd="gpi2")
    target.activate(d)
    d.set(1)
    assert d.get() == 1
    d.set(0)
    assert d.get() == 0

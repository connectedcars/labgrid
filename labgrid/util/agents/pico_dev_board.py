import serial
from time import sleep

class USBPicoDevBoard:
    allowed_commands = [
        "dut_power",
        "dut_ignition",
        "dut_usb_power",
        "dut_recovery_mode", # this returns value for two pins, but currently we only check if at least one is on.
        "dut_uart_power",
        "dut_uart_data",
        "gpi1",
        "gpi2"
    ]

    def set_output(self, path, cmd, status):
        if cmd not in self.allowed_commands:
            raise ValueError(f"Unknown command {cmd}")
        msg = f'{cmd}_on\n' if status else f'{cmd}_off\n'
        with serial.Serial(path, 9600, timeout=5) as ser:
            ser.write(msg.encode())
            ser.read_until().decode() # eat echo

    def get_output(self, path, cmd):
        msg = f'{cmd}_state\n'
        with serial.Serial(path, 9600, timeout=5) as ser:
            ser.write(msg.encode())
            ser.read_until().decode() # eat echo
            sleep(1)
            data = ser.read_until().decode()
            state = 1 if ": on" in data else 0
        return state

_devboards = {}

def _get_devboard(path):
    if (path) not in _devboards:
        _devboards[(path)] = USBPicoDevBoard()
    return _devboards[(path)]

def handle_set(path, cmd, status):
    devboard = _get_devboard(path)
    devboard.set_output(path, cmd, status)

def handle_get(path, cmd):
    devboard = _get_devboard(path)
    return devboard.get_output(path, cmd)

methods = {
    "set": handle_set,
    "get": handle_get,
}

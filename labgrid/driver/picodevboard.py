import attr

from .common import Driver
from ..factory import target_factory
from ..step import step
from ..protocol import DigitalOutputProtocol
from ..util.agentwrapper import AgentWrapper
from ..resource.remote import NetworkPicoDevBoard


@target_factory.reg_driver
@attr.s(eq=False)
class PicoDevBoardDriver(Driver, DigitalOutputProtocol):
    bindings = {
        "board": {"PicoDevBoard", "NetworkPicoDevBoard"},
    }
    cmd = attr.ib(validator=attr.validators.instance_of(str))

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.wrapper = None

    def on_activate(self):
        if isinstance(self.board, NetworkPicoDevBoard):
            host = self.board.host
        else:
            host = None
        self.wrapper = AgentWrapper(host)
        self.proxy = self.wrapper.load('pico_dev_board')

    def on_deactivate(self):
        self.wrapper.close()
        self.wrapper = None
        self.proxy = None

    @Driver.check_active
    @step(args=['status'])
    def set(self, status):
        self.proxy.set(self.board.path, self.cmd, status)

    @Driver.check_active
    @step(result=True)
    def get(self):
        status = self.proxy.get(self.board.path, self.cmd)
        return status

from . import simple as simple

class MQTTClient(simple.MQTTClient):
    DELAY: int
    DEBUG: bool
    def delay(self, i) -> None: ...
    def log(self, in_reconnect, e) -> None: ...
    def reconnect(self): ...
    def publish(self, topic, msg, retain: bool = ..., qos: int = ...): ...
    def wait_msg(self): ...
    def check_msg(self, attempts: int = ...): ...

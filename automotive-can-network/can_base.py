import can
import cantools
import threading
import time
import logging
from pathlib import Path

DBC_PATH = Path(__file__).parent / "vehicle_network.dbc"

BUS_MAP = {
    "powertrain": "vcan0",
    "chassis": "vcan1",
    "body": "vcan2",
    "infotainment": "vcan3"
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S"
)

class BaseECU:

    def __init__(self, ecu_name: str, bus_name: str):
        self.name = ecu_name
        self.bus_name = bus_name
        self.channel = BUS_MAP[bus_name]
        self.log = logging.getLogger(ecu.name)
        self.db = cantools.database.load_file(str(DBC_PATH))
        self.bus = None
        self.running = False
        self.thread = []
        self.transmit_jobs = []
    
    def connect(self):
        self.bus = can.interface.Bus(
            channel=self.channel,
            interface="socketcan"
        )
        self.log.info(f"Connected to {self.channel} ({self.bus_name})")
    
    def encode_and_send(self, msg_name: str, signals : dict):
        try:
            msg_def = self.db.get_message_by_name(msg_name)
            data = msg_def.encode(signals)
            frame = can.Message(
                arbitration_id=msg_def.frame_id,
                data=data,
                is_extended_id=False
            )
            self.bus.send(frame)
        except Exception as e:
            self.log.error(f"Failed to send {msg_name}: {e}")

    def _periodic_sender(self, msg_name: str, period_s: float, data_fn):
        self.log.info(f"Starting TX: {msg_name} @ {1/period_s:.0f} Hz")
        while self.running:
            signals = data_fn()
            self.encode_and_send(msg_name, signals)
            time.sleep(period_s)
    
    def start(self):
        self.connect()
        self.running = True
        for (msg_name, period_s, data_fn) in self.transmit_jobs:
            t = threading.Thread(
                target=self._periodic_sender, 
                args=(msg_name, period_s, data_fn),
                daemon=True
            )
            t.start()
            self.log.threads.append(t)
        self.log.info(f"ECU started - {len(self.transmit_jobs)} TX job(s)")
    
    def stop(self):
        self.running = False
        if self.bus:
            self.bus.shutdown()
        self.log.info("ECU stopped")


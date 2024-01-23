import logging
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timedelta

log = logging.getLogger(name=__name__)


@dataclass
class Chrono:
	name: str
	start_time: datetime = None
	stop_time: datetime = None

	def __post_init__(self):
		self.start()

	def start(self) -> "Chrono":
		self.start_time = datetime.now()
		self.stop_time = None
		log.debug(f"Chrono {self.name}: start at {self.start_time}")
		return self

	def stop(self) -> "Chrono":
		if self.stop_time is None:
			self.stop_time = datetime.now()
			log.debug(f"Chrono {self.name}: stop at {self.stop_time}")
		return self

	def get_duration(self) -> timedelta:
		if self.stop_time is not None:
			stop_time = self.stop_time
		else:
			stop_time = datetime.now()
		duration = stop_time - self.start_time
		log.debug(f"Chrono {self.name}: duration is {duration}")
		return duration

	def __str__(self):
		return f"{self.__class__.__name__}(name=\"{self.name}\", duration=\"{str(self.get_duration())}\")"


if __name__ == "__main__":
	log.setLevel(logging.INFO)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	handler = logging.StreamHandler(sys.stdout)
	handler.setLevel(logging.DEBUG)
	handler.setFormatter(formatter)
	log.addHandler(handler)

	c = Chrono(name="a")
	log.info(f"Chrono already started but not finished: {c}")
	time.sleep(0.5)
	log.info(f"Chrono duration so far: {c.get_duration()}")
	time.sleep(0.5)
	log.info(f"Chrono duration after stop: {c.stop().get_duration()}")

	log.info(f"Chrono restart: {c.start()}")
	time.sleep(0.5)
	log.info(f"Chrono duration so far: {c.get_duration()}")
	time.sleep(0.5)
	log.info(f"Chrono duration: {c.get_duration()}")

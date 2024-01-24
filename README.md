# chrono
Python lib to measure a duration
    
    >>> from chrono import Chrono
    >>> a_chrono = Chrono("a simple chrono")
    >>> a_chrono
    Chrono(name='a simple chrono', start_time=datetime.datetime(2024, 1, 24, 16, 56, 39, 804534), stop_time=None)
    >>> a_chrono.get_duration()
    datetime.timedelta(seconds=15, microseconds=392807)
    >>> a_chrono.stop()
    Chrono(name='a simple chrono', start_time=datetime.datetime(2024, 1, 24, 16, 56, 39, 804534), stop_time=datetime.datetime(2024, 1, 24, 16, 57, 2, 858345))
    >>> a_chrono.get_duration()
    datetime.timedelta(seconds=23, microseconds=53811)

from reviewboard.signals import initializing


def connect_signals(**kwargs):
    """
    Listens to the ''initializing'' signal and tells other modules to
    connect their signals. This is done so as to guarantee that django
    is loaded first.
    """
    from rbwebhooks import event_manager
    
    event_manager.connect_signals()
        

initializing.connect(connect_signals)

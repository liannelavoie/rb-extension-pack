# CIA extension for Review Board.
from reviewboard.extensions.base import Extension


class WebhooksExtension(Extension):
    is_configurable = True

    def __init__(self):
        Extension.__init__(self)

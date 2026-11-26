from unittest.mock import patch

import pytest

from main import App


# asks user to select deck
#   call loader

def test_loop_keeps_calling_router():
    class StopLoop(Exception): # exceptions interrupts python's loops
        pass

    app = App()
    with patch.object(app, "router", side_effect=[None, None, StopLoop]) as router: #replaces `app.router` with a mock
        with pytest.raises(StopLoop):
            app.loop()

    assert router.call_count == 3

def test_router_opens_welcome_page_on_startup():
    app = App()

    with patch.object(app, "page_welcome") as welcome:
        app.router()

    welcome.assert_called_once_with()

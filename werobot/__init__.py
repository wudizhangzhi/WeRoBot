__version__ = '1.2.1'
__author__ = 'whtsky & yueyatianchong'
__license__ = 'MIT'

__all__ = ["WeRoBot"]

try:
    from werobot.robot import WeRoBot
except ImportError:  # pragma: no cover
    pass  # pragma: no cover

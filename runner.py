#!/usr/bin/env python
from board import Board, LogicException

# this needs to be smarter soon
_board = Board('simple.karelmap')

def _refresh(callback):
    def inner():
        res = callback()
        _board.draw()
        return res
    return inner

move = _refresh(lambda: _board.move())
turn_left = _refresh(lambda: _board.turn_left())
pick_beeper = _refresh(lambda: _board.pick_beeper())
put_beeper = _refresh(lambda: _board.put_beeper())
front_is_clear = _refresh(lambda: _board.front_is_clear())
right_is_clear = _refresh(lambda: _board.right_is_clear())
left_is_clear = _refresh(lambda: _board.left_is_clear())
beeper_is_present = _refresh(lambda: _board.beeper_is_present())

def execute(callback):
    try:
        _board.start_screen()
        _board.draw()
        callback()
        return callback
    except LogicException, e:
        _board.draw_exception(e)
    except Exception, e:
        raise e
    finally:
        _board.end_screen()
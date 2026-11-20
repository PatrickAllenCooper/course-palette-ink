from app import normalize
from candidate import ink

def check():
    bg=normalize('white')
    assert ink(bg,'#999999',['#777777','#767676','#000000'])=='#767676'
    assert ink(bg,'#999999',['#ffffff']) is None
    assert ink(bg,'#010101',['#010102','#010100'])=='#010102'

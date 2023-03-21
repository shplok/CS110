import stdio
import stdarray
from datetime import datetime

DAY = 24

stdio.writeln("How Many Assignments Would You Like To Report?")
_assignNum = stdio.readInt()

_NameSec = stdarray.create1D(_assignNum, None)
_DueSec = stdarray.create1D(_assignNum, None)
_Importance = stdarray.create1D(_assignNum, None)

for i in range(_assignNum):
    stdio.writeln("Name of Assignment " + str(i + 1))
    _NameSec[i] = stdio.readString()
    stdio.writeln("How Many Days Until " + str(_NameSec[i]) + " is Due?")
    _DueSec[i] = stdio.readInt()
    if _DueSec[i] > 14:
        _Importance[i] = "You Have Time"
    if 14 > _DueSec[i] >= 10:
        _Importance[i] = "!"
    if 10 > _DueSec[i] >= 5:
        _Importance[i] = "!!"
    if 5 > _DueSec[i] >= 3:
        _Importance[i] = "!!!"
    if 3 > _DueSec[i] >= 1:
        _Importance[i] = "!!!!"
    if 1 > _DueSec[i]:
        _Importance[i] = "Turn in Today"
    if _DueSec[i] <= 0:
        _Importance[i] = "Overdue"

now = datetime.now()
current_time = now.strftime("%D:  %H:%M")


stdio.writeln(current_time)
stdio.writeln(_NameSec)
stdio.writeln(_Importance)
stdio.write(_DueSec)
stdio.writeln(" Days Left")

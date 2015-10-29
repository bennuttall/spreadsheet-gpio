from gpiozero import PWMLED
from signal import pause
from connect import open_worksheet, read_cell_continuous

wks = open_worksheet("GPIO Zero")

led = PWMLED(2)

led.source = read_cell_continuous(wks, 1, 1)

pause()

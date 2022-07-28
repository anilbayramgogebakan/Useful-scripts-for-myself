:: This file used to syncronize your computer time with the Internet time.
:: It is used to solve to wrong Windows time problem starting Windows OS after using Ubuntu
:: in dual boot computers. This script runs every time I started Windows OS.

net start w32time
w32tm /query /peers
w32tm /resync /nowait
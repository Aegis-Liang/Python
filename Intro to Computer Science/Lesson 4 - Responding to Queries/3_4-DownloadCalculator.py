# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def convert_seconds(a):
    r = ""
    
    h = int(a // 3600)
    if h == 1:
        r = r + str(h) + " hour, "
    else:
        r = r + str(h) + " hours, "
    
    m = int(a % 3600 // 60)
    if m == 1:
        r = r + str(m) + " minute, "
    else:
        r = r + str(m) + " minutes, "
    
    s = a % 60
    if s == 1:
        r = r + str(s) + " second"
    else:
        r = r + str(s) + " seconds"
        
    return r

def convert_unit(u):
    r = 1
    if u[0] == 'k':
        r = r * 2 ** 10
    elif u[0] == 'M':
        r = r * 2 ** 20
    elif u[0] == 'G':
        r = r * 2 ** 30
    elif u[0] == 'T':
        r = r * 2 ** 40
    
    if u[1] == 'B':
        r = r * 8
    
    return r
    
def download_time(tn, tu, sn, su):
    tt = tn * convert_unit(tu)
    st = sn * convert_unit(su)
    
    return convert_seconds(float(tt)/st)



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable



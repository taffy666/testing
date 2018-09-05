f = open("ansible.cfg")
try:
    for line in f:
        print line
finally:
    f.close()

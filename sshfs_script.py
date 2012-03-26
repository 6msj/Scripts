import os 

print "Would you like to mount (1) or unmount (2)?"
choice = int(raw_input("< "))
if choice == 1:
    return_value = os.system('sshfs james@server:/media/WII/Music/ ~/sshmusic/')
    if return_value == 0:
        os.system('echo "Mount Successful"')
elif choice == 2:
    return_value = os.system('fusermount -u ~/sshmusic/')
    if return_value == 0:
        os.system('echo "Unmount Successful"')
else:
    print "No valid entry."

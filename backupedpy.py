import os

# backing up vim
def backup_VIM(choice):
    if choice == 'y':
        os.system('sudo rsync -tuP --modify-window=1 /home/jamesarch/.vimrc /etc/vimrc')
        os.system('echo "Backed up .vimrc to /etc/vimrc"')

        os.system('rsync -tuP --modify-window=1 --delete /home/jamesarch/.vim/ /media/Main/.vim/vimrc')
        os.system('echo "Backed up vimrc to Main hard-drive."')

        os.system('sudo rsync -turP --modify-window=1 --delete /home/jamesarch/.vim/ /media/Main/.vim/')
        os.system('echo "Backed up .vim to Main hard-drive."')
    elif choice == 'n':
        print "Didn't back up vim."
    else:
        print "You didn't enter anything (worthwhile)."

# backing up emacs
def backup_EMACS(choice):
    if choice == 'y':
        os.system('rsync -tuP --modify-window=1 /home/jamesarch/.emacs /home/jamesarch/.emacs.d/emacs')
        os.system('echo "Backed up .emacs to emacs directory.')

        os.system('sudo rsync -turP --modify-window=1 --delete /home/jamesarch/.emacs.d/ /media/Main/.emacs.d/')
        os.system('echo "Backed up emacs to Main hard-drive."')

    elif choice == 'n':
        print "Didn't back up emacs."
    else:
        print "You didn't enter anything (worthwhile)."

# backing up to git
def backup_GIT(choice):
    if choice == 'y':
        os.system('cd /home/jamesarch/.vim/')
        os.system('git add -A')
        os.system('git commit -m \'backup\'')
        os.system('git push origin master')

        os.system('cd /home/jamesarch/.emacs.d/')
        os.system('git add -A')
        os.system('git commit -m \'backup\'')
        os.system('git push origin master')
    else:
        os.system('echo "Didn\'t back up to git" ')



# MAIN
print "Would you like to back up everything? (y/n) "
CHOICE = raw_input("< ")
if(CHOICE == 'y'):
    backup_VIM(CHOICE)
    backup_EMACS(CHOICE)
    backup_GIT(CHOICE)
else:
    print "Would you like to backup vim? (y/n) " #for vim
    vim_Choice = raw_input("< ")
    backup_VIM(vim_Choice)

    print "Would you like to backup emacs? (y/n) " #for emacs
    emacs_Choice = raw_input("< ")
    backup_EMACS(emacs_Choice)

    print "Would you like to backup to git? (y/n) " #for git
    git_Choice = raw_input("< ")
    backup_GIT(git_Choice)


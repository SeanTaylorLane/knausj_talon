tag: terminal
-
# tags should be activated for each specific terminal in the respective talon file

lisa: 
    # user.terminal_list_directories()
    insert("ls ")
    # key(enter)
lisa all: 
    insert("ls -a")
    key(enter)
    # user.terminal_list_all_directories()
# katie [<user.text>]: user.terminal_change_directory(text or "")
# katie parent: user.terminal_change_directory("../")
katie:
    insert("cd ")
katie parent: 
    insert("cd ../")
    key(enter)
katie root: user.terminal_change_directory_root()
clear screen: user.terminal_clear_screen()
run last: user.terminal_run_last()
rerun [<user.text>]: user.terminal_rerun_search(text or "")
rerun search: user.terminal_rerun_search("")
rerun exit:
    key(ctrl-g)
kill all: user.terminal_kill_all()
kill that:
    key(ctrl-c)

adb:
    insert("adb.exe ")
adb shell:
    insert("adb.exe shell ")
    # key(enter)
adb push:
    insert("adb.exe push ")


# scripting:
#   insert("cd /mnt/c/Users/Sean/AppData/Roaming/talon/")
#   key(enter)

# vi|v|the: insert("vim ")
# vi|v|the save:
#   insert(":w")
#   key(enter)
# vi|v|the exit:
#   insert(":x")
#   key(enter)
# vi|v|the quit:
#   insert(":q")
#   key(enter)
# vi|v|the next: insert("gt")
# vi|v|the last: insert("gT")

# recurs|rodeo: key(ctrl-r)

grep: insert("grep ")

# tmax new:
#   key(ctrl-b)
#   key(c)
# tmax next:
#   key(ctrl-b)
#   key(n)
# tmax last:
#   key(ctrl-b)
#   key(p)
# tmax kill:
#   key(ctrl-b)
#   key(x)
# tmax detach:
#   key(ctrl-b)
#   key(d)

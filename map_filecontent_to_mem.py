import subprocess
import mmap
import time
import os

def execute_command(cmd):
    subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)


def pre_run():
    cmd = "dd if=/dev/zero of=demo.bin bs=1024 count=1024"
    execute_command(cmd)
    #time.sleep(1)


def post_run():
    cmd = "rm -f demo.bin"
    execute_command(cmd)
    #time.sleep(1)


def mmap_the_file_content():
    f = open('demo.bin', 'r+b')
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print m[0]
    print m[10:20]
    m[0] = '\x88'   # u can use "od -x demo.bin" to check the filecontent
    print type(m)

if __name__ == '__main__':
    pre_run()
    os.wait()
    mmap_the_file_content()
    #post_run()

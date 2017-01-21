from subprocess import Popen, PIPE
from select import select
import re

class UdevAdm:
    def __init__(self, timeout=None):
        self.timeout = timeout
        self.p = Popen(['udevadm', 'monitor', '--udev', '--environment'],
                       stdout=PIPE)

    def __enter__(self):
        p = self.p
        timeout = self.timeout

        devs = []

        while True:
            if not select([p.stdout], [], [], timeout)[0]:
                yield devs
                timeout = self.timeout
                devs = []

            line = p.stdout.readline().decode('utf-8')
            if re.match('UDEV\s*\[.*\]\s*add', line):
                action = 'add'
            elif re.match('UDEV\s*\[.*\]\s*remove', line):
                action = 'remove'
            else:
                continue

            dev = {'__action__': action}

            while True:
                if not select([p.stdout], [], [], timeout)[0]:
                    yield devs
                    timeout = self.timeout
                    devs = []

                line = p.stdout.readline().decode('utf-8')
                m = re.match('(.*)=(.*)', line)
                if m is None:
                    break

                key, val = m.groups()
                dev[key] = val

            devs.append(dev)
            timeout = 0

    def __exit__(self, *_):
        self.p.terminate()

if __name__ == '__main__':
    with UdevAdm(3) as ua:
        print(next(ua))

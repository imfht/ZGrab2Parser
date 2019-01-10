import sys
import threading
from multiprocessing.dummy import Pool

from Plugins import ESPlugin, MySQLPlugin

lock = threading.Lock()
PRINT_ONLY_SUCCESS = False


def print_response(response):
    if (not response.success) and PRINT_ONLY_SUCCESS:
        return
    lock.acquire()
    print(PRINT_ONLY_SUCCESS)
    lock.release()


def run_es(arg, ):
    ip, port = arg
    response = ESPlugin.parse_it(ip, port)
    print_response(response)


def run_mysql(arg):
    ip, port, user, password = arg
    response = MySQLPlugin.parse_it(ip=ip, port=port, password=password, user=user, timeout=20)
    print_response(response)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py filename")
    ip_port_file = open(sys.argv[1])
    _ = []
    if sys.argv[3] == 'es':
        for line in ip_port_file.readlines():
            ip, port = line[0:-1].split(':')
            _.append((ip, port))
        pool = Pool(processes=32)
        pool.map(run_es, _)
        pool.close()
        pool.join()

    elif sys.argv[3] == 'mysql':  # mysql ip:port:username:password
        for line in ip_port_file.readlines():
            ip, port, user, password = line[0:-1].split(':')
            _.append((ip, port, user, password))
        pool = Pool(processes=32)
        pool.map(run_mysql, _)
        pool.close()
        pool.join()
    else:
        print("only support mysql & es")

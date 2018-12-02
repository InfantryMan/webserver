import argparse

from server import Server
from config import Config

CONFIG_PATH = '/etc/httpd.conf'

if __name__ == '__main__':
    config = Config(CONFIG_PATH)

    parser = argparse.ArgumentParser()
    parser.add_argument('--ncpu', type=int, help='number of processes', default=config.cpu_number)
    parser.add_argument('--root', type=str, help='html page root', default=config.root)
    args = parser.parse_args()

    if args.ncpu is None or args.root is None:
        raise RuntimeError('ncpu or root was not specified')

    server = Server(args.ncpu, args.root, config.address_port, config.receive_data_size, config.queue)
    server.start()

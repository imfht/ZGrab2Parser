import sys

from elasticsearch import Elasticsearch

from Plugins.ElasticSearch import parse_it

if __name__ == '__main__':
    es = Elasticsearch()
    if len(sys.argv) != 2:
        print("Usage: python main.py filename")
    ip_port_file = open(sys.argv[1])
    for line in ip_port_file.readlines():
        ip, port = line[0:-1].split(':')
        response = parse_it(ip, port)
        es.index(index="es_leak", doc_type="default", body=response.__dict__)

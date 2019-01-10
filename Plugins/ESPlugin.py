import requests

from Plugins import Result


def parse_it(ip, port, https=False, timeout=5):
    base_url = 'https://%s:%s' % (ip, port) if https else 'http://%s:%s/' % (ip, port)
    cat_url = base_url + '_cat/indices?v'
    try:
        req = requests.get(cat_url, timeout=timeout)
        text = req.text
        info = {"index_count": len(text.split("\n")), "indices": []}
        try:
            for line in text.split("\n"):
                if len(line.split()) != 10:
                    continue
                health, status, index, uuid, pri, rep, count, deleted, size, pri_store_size = line.split()
                index_info = {
                    "health": health,
                    "status": status,
                    "index": index,
                    "uuid": uuid,
                    "pri": pri,
                    "rep": rep,
                    "count": count,
                    "deleted": deleted,
                    "size": size,
                    "pri_store_size": pri_store_size
                }
                sample = {}
                try:
                    req = requests.get(url=base_url + '/' + index + "/_search")
                    sample = req.json()
                except Exception as e:
                    print(e)
                index_info['sample'] = req.json()
                info["indices"].append(index_info)

        except Exception as e:
            print(e)
        return Result(ip, port, info=info, success=True)
    except Exception as e:
        print(e)
        return Result(success=False, ip=ip, port=port, info={"failed"})


if __name__ == '__main__':
    print(parse_it(ip='61.13.197.6', port=9200))

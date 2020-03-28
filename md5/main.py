import hashlib


def get_md5(path):
    with(open(path, encoding="utf-8")) as f:
        for line in f:
            line = line.encode('utf-8')
            md5 = hashlib.md5(line.strip())
            yield md5.hexdigest()


if __name__ == '__main__':
    for md5_line in get_md5("file.txt"):
        print(md5_line)


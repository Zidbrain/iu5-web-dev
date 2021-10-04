from typing import Any, Dict, Generator, Union

def field(items: list[dict], *args) -> Generator[Union[Any, dict], None, None]:
    assert len(args) > 0

    for item in items:
        if (len(args) == 1):
            if (item.get(args[0])): yield item[args[0]]
        else:
            ret = {}
            for arg in args:
                if (item.get(arg)): ret[arg] = item[arg]
            if (len(ret.items()) != 0): yield ret
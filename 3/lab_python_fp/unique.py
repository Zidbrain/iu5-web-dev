class Unique(object):
    def __init__(self, items, **kwargs):
        self._iterator = iter(items)
        if (kwargs.get('ignore_case') is None):
            self._ignoreCase = False
        else:
            self._ignoreCase = kwargs.get('ignore_case')

    def __next__(self):
        item = next(self._iterator)

        try:
            if (self._ignoreCase == True):
                item = item.casefold()
        except: pass

        if (item not in self._found):
            self._found.append(item)           
            return item
        
        return Unique.__next__(self)

    def __iter__(self):
        self._found = list()
        return self
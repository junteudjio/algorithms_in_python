from hash_map_base import HashMapBase

__author__ = 'Junior Teudjio'


class ProbeHashMap(HashMapBase):
    _AVAILABLE_MARKER = object()

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is self._AVAILABLE_MARKER


    def _find_slot(self, j, key):
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j  # mark this as first avail
                if self._table[j] is None:
                    return (False, firstAvail)  # search has failed
            elif key == self._table[j]._key:
                return (True, j)  # found a match
            j = (j + 1) % len(self._table)


    def _set_bucket_item(self, bucket_idx, key, value):
        found, idx = self._find_slot(bucket_idx, key)
        if not found:
            self._table[idx] = self._Item(key, value)
            self._number_of_elements += 1
        else:
            self._table[idx]._value = value


    def _get_bucket_item(self, bucket_idx, key):
        found, idx = self._find_slot(bucket_idx, key)
        if not found:
            raise KeyError('key: %s not found' % repr(key))
        return self._table[idx]._value

    def _del_bucket_item(self, bucket_idx, key):
        found, idx = self._find_slot(bucket_idx, key)
        if not found:
            raise KeyError('key: %s not found' % repr(key))

        self._table[idx] = self._AVAILABLE_MARKER
        self._number_of_elements -= 1

    def __iter__(self):
        for idx, item in enumerate(self._table):
            if self._is_available(idx):
                yield item._key

    def __str__(self):
        res = []
        for idx, item in enumerate(self._table):
            if not self._is_available(idx):
                key, value = item._key, item._value
                res.append('%s -> %s'%(key, value))
        return ' | '.join(res)



if __name__ == '__main__':
    prob_map = ProbeHashMap()
    prob_map['student_1'] = 'Junior'
    print prob_map
    prob_map['student_2'] = 'Adam'
    prob_map['student_3'] = 'Remi'
    print prob_map
    del prob_map['student_3']
    print prob_map
    prob_map['student_4'] = 'James'
    print prob_map
    prob_map['student_4'] = 'John'
    print prob_map

from map_base import MapBase

__author__ = 'Junior Teudjio'


class UnsortedTableMap(MapBase):
    def __init__(self):
        self._table = []

    def __setitem__(self, key, value):
        for item in self._table:
            if item._key == key:
                item._value = value
                return

        self._table.append(MapBase._Item(key, value))

    def __getitem__(self, key):
        for item in self._table:
            if item._key == key:
                return item._value
        raise KeyError('key: %s not found'% repr(key))


    def __delitem__(self, key):
        found_idx = -1
        for i, item in enumerate(self._table):
            if item._key == key:
                found_idx = i
                break
        if found_idx > -1:
            self._table.pop(found_idx)
        else:
            raise KeyError('key: %s not found' % repr(key))

    def __len__(self):
        return len(self._table)


    def __iter__(self):
        for item in self._table:
            yield item._key, item._value
    
    def __str__(self):
        res = []
        for key, value in self:
            res.append( '%s -> %s'%( str(key), str(value)) )
        return ' | '.join(res)
            
            
if __name__ == '__main__':
    u_map = UnsortedTableMap()
    u_map['student_1'] = 'Junior'
    print u_map
    u_map['student_2'] = 'Adam'
    u_map['student_3'] = 'Remi'
    print u_map
    del u_map['student_3']
    print u_map
    u_map['student_4'] = 'James'
    print u_map
    u_map['student_4'] = 'John'
    print u_map
    
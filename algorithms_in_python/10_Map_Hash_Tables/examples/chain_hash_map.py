from hash_map_base import HashMapBase
from unsorted_table_map import UnsortedTableMap

__author__ = 'Junior Teudjio'


class ChainHashMap(HashMapBase):
    def _set_bucket_item(self, bucket_idx, key, value):
        bucket = self._table[bucket_idx]
        if bucket is None:
            self._table[bucket_idx] = UnsortedTableMap()

        previous_bucket_size = len(self._table[bucket_idx])
        self._table[bucket_idx][key] = value
        after_bucket_size = len(self._table[bucket_idx])
        if after_bucket_size > previous_bucket_size:
            self._number_of_elements += 1


    def _get_bucket_item(self, bucket_idx, key):
        bucket = self._table[bucket_idx]
        if bucket is None:
            raise KeyError('key: %s not found' % repr(key))
        return self._table[bucket_idx][key] # may still raise an exception

    def _del_bucket_item(self, bucket_idx, key):
        bucket = self._table[bucket_idx]
        if bucket is None:
            raise KeyError('key: %s not found' % repr(key))

        previous_bucket_size = len(self._table[bucket_idx])
        del self._table[bucket_idx][key]  # may still raise an exception
        after_bucket_size = len(self._table[bucket_idx])
        if after_bucket_size < previous_bucket_size:
            self._number_of_elements -= 1

    def __iter__(self):
        for bucket in self._table:
            if bucket is None:
                continue
            for key in bucket:
                yield key

    def __str__(self):
        res = []
        for bucket in self._table:
            if bucket is None:
                continue
            res.append(str(bucket))
        return ' | '.join(res)


if __name__ == '__main__':
    chain_map = ChainHashMap()
    chain_map['student_1'] = 'Junior'
    print chain_map
    chain_map['student_2'] = 'Adam'
    chain_map['student_3'] = 'Remi'
    print chain_map
    del chain_map['student_3']
    print chain_map
    chain_map['student_4'] = 'James'
    print chain_map
    chain_map['student_4'] = 'John'
    print chain_map

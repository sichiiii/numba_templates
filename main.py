import time
import numpy as np
from numba import njit

arr = np.array([(1, 2)], dtype=[('a1', 'f8'), ('a2', 'f8')])
fields_gl = ('a1', 'a2')

@njit
def get_field_sum(rec):
    fields_lc = ('a1', 'a2')
    field_name1 = fields_lc[0]
    field_name2 = fields_gl[1]
    return rec[field_name1] + rec[field_name2]

if __name__ == '__main__':
    start_time = time.time()
    print(get_field_sum(arr[0]))
    print("--- %s seconds ---" % (time.time() - start_time))

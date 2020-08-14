class MatrixMcls(type):
    def __getitem__(cls, data):
        return cls(data)
    def __repr__(self):
        return "M[]"


class M(metaclass=MatrixMcls):
    __slots__ = ("data", "shape", "dims", "dtype")

    def __init__(self, data):
        try:
            data = list(data)
        except TypeError:
            self.shape = ()
        else:
            lengths = {}
            for d in data:
                try:
                    lengths[len(d)] = d
                except TypeError:
                    self.shape = len(data),
                    lengths[None] = d
            if len(lengths)>1:
                raise TypeError(f"Inconsistent column numbers: {lengths}")
            if lengths:
                self.shape = len(data), next(iter(lengths))
        self.dims = len(self.shape)
        self.data = data

    def __repr__(self):
        if (dims:=self.dims) == 2:
            content = ",\n  ".join(f"{d}" for d in self.data)
        elif dims == 1:
            content = ", ".join(f"{d}" for d in self.data)
        else:
            content = self.data
        return f'M[{content}]'


if __name__=="__main__":
    print(M)
    m1 = M[[1,2,3],
          [4,5,6],
          [7,8,9]]
    print(m1, m1.shape, m1.dims)
    m2 = M[1,2,3]
    print(m2, m2.shape, m2.dims)
    m3 = M[1]
    print(m3, m3.shape, m3.dims)
    m4 = M[[[1,2,3],
          [4,5,6],
          [7,8,9]],
           [[1,2,3],
            [4,5,6],
            [7,8,9]],
           [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]]
    print(m4, m4.shape, m4.dims)
    # expect error
    try:
        m5 = M[[1,2,3],[1,2]]
    except TypeError:
        pass
    else:
        raise Exception("m5 = M[[1,2,3],[1,2]] did not raise error")
    # expect error
    try:
        m6 = M[1,[1,2]]
    except TypeError:
        pass
    else:
        raise Exception("m6 = M[1,[1,2]] did not raise error")

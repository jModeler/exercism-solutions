def saddle_points(matrix):
    if matrix == []:
        return []
    else:        
        # test if matrix is regular
        lens = [len(mat) for mat in matrix]
        unique = list(set(lens))
        if len(unique) != 1:
            raise ValueError("irregular matrix")
        else:
            result = []
            rows = len(matrix)
            cols = len(matrix[0])
            for ii in range(rows):
                row_max_val = max(matrix[ii])
                indexes = [kk for kk in range(cols) if matrix[ii][kk] == row_max_val]
                for jj in indexes:
                    column = [matrix[ll][jj] for ll in range(rows)]
                    col_min_val = min(column)
                    if row_max_val == col_min_val:
                        result.append({"row": (ii + 1), "column": (jj + 1)})
        return result

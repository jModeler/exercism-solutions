# using a dictionary to store digit patterns since this is a limited number
# I'll be using this as a  lookup table
DIGIT_PATTERNS = {
    (
        " _ ",
        "| |",
        "|_|",
        "   ",
    ): "0",
    (
        "   ",
        "  |",
        "  |",
        "   ",
    ): "1",
    (
        " _ ",
        " _|",
        "|_ ",
        "   ",
    ): "2",
    (
        " _ ",
        " _|",
        " _|",
        "   ",
    ): "3",
    (
        "   ",
        "|_|",
        "  |",
        "   ",
    ): "4",
    (
        " _ ",
        "|_ ",
        " _|",
        "   ",
    ): "5",
    (
        " _ ",
        "|_ ",
        "|_|",
        "   ",
    ): "6",
    (
        " _ ",
        "  |",
        "  |",
        "   ",
    ): "7",
    (
        " _ ",
        "|_|",
        "|_|",
        "   ",
    ): "8",
    (
        " _ ",
        "|_|",
        " _|",
        "   ",
    ): "9",
}


def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    else: 
        sub_grids = [input_grid[ii:ii+4] for ii in range(0, len(input_grid), 4)]
        # get the length of input columns for the next check
        columns = len(input_grid[0]) # assuming all input columns are the same length, which is the expectation
        if columns % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")
        else:
            # prepare sub_grids for processing
            processed_input = []
            for jj in sub_grids:
                ll = 0
                temp_input = []
                while ll < len(jj[0]):
                    temp_grid = []
                    for kk in jj:
                        temp_grid.append(kk[ll: ll+3])
                    ll += 3
                    temp_input.append(temp_grid)
                processed_input.append(temp_input)
    # start processing the input
    result = ""
    for ii in processed_input:
        for jj in ii:
            result = "".join([result, DIGIT_PATTERNS.get(tuple(jj), "?")])
        if ii != processed_input[-1]:
            result = "".join([result, ","])

    return result
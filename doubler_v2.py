import argparse

write_block_size = 5000
out_file = 'marching_doubler.txt'

def marching_doubler_v2(rl, sl):
    """
    Writes the Marching Doubler sequence to a file. We are assuming that file we want to write to is called ./marching_double.txt.
    We are using a buffer of 5000 characters to write to the file to avoid extensive disk accesses. This is based on the assumption
    that the file size is less than 100MB. This value can be adjusted to match required disk access efficiency.
    It is assumed that the run length should be at least two. This method uses Python's built in buffered file write instead of a
    manual buffer.


    Parameters
    ----------
    rl : integer
        The length of a run
    sl : integer
        The total number of terms in the series

    """
    if rl < 2:
        return

    rs = range(1, rl)  # generate a sequence for run length less one, e.g. if rl == 4 then rs = [1, 2, 3]
    i = 0
    with open(out_file, 'w', write_block_size) as file_writer:
        while i < sl:
            for j in range(rl - 1):
                if (i // rl) % (rl - 1) == j:
                    file_writer.write(f'{rs[j]},')
                    i += 1
                    if i == sl:
                        return
                file_writer.write(f'{rs[j]},')
                i += 1
                if i == sl:
                    return

if __name__ == "__main__":
    help_str = 'doubler_v2.py -r <run length> -s <sequence length>'
    parser = argparse.ArgumentParser(usage=help_str)
    parser.add_argument('-r', '--run_length', metavar='run length', type=int, required=True, help='The length of a run')
    parser.add_argument('-s', '--seq_length', metavar='sequence length', type=int, required=True, help='The total number of terms in the series')
    args = parser.parse_args()
    
    marching_doubler_v2(args.run_length, args.seq_length)

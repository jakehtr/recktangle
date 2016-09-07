#! usr/bin/env python3

"""
recktangle.py - Creates a rectangle made up of a given word!
"""


def divide(x, y):
    if x / y == x // y:
        return x // y
    return x // y + 1


def recktangle(word, width, height):
    left_right = list()
    top_rows = list()
    final_reckt = str()

    # creating the vertical rows
    for j in range(len(word) - 2):
        new_row = str()
        new_row += '{0}{1}{2}{1}'.format(word[j + 1],
                                         ' ' * (2 * len(word) - 3),
                                         word[-2 - j]) * divide(width, 2)
        if width % 2 == 0:
            new_row += '{}'.format(word[j + 1])

        left_right.append('\n{}'.format(new_row.strip()))

    # creating the horizontal rows
    for i in range(2):
        if i % 2 == 0:
            word_ = word
        else:
            word_ = word[::-1]
        top = '{}'.format(word_[0])
        for j in range(width):
            if j % 2 == 0:
                top += ' {}'.format(' '.join(word_[1:]))
            else:
                top += ' {}'.format(' '.join(word_[:-1][::-1]))
        top_rows.append(top)

    for k in range(height):
        if k % 2 == 0:
            left_right_ = left_right
        else:
            left_right_ = left_right[::-1]

        final_reckt += '{}{}\n'.format(top_rows[k % 2], ''.join(left_right_))
    final_reckt += top_rows[height % 2]  # add bottom row

    print(final_reckt)

if __name__ == '__main__':
    recktangle('fathom', 4, 4)

#! usr/bin/env python3

"""
recktangle.py - Creates a rectangle made up of a given word!
"""


def divide(x, y):
    if x / y == x // y:
        return x // y
    return x // y + 1


def recktangle(word, width, height):
    v_rows = list()
    h_rows = list()
    final_reckt = str()

    if len(word) == 1:
        return '\n{}\n'.format(word)

    # creating the vertical rows
    for j in range(len(word) - 2):
        v_row = str()
        v_row += '{0}{1}{2}{1}'.format(word[j + 1],
                                       ' ' * (2 * len(word) - 3),
                                       word[-2 - j]) * divide(width, 2)
        if width % 2 == 0:
            v_row += '{}'.format(word[j + 1])

        v_rows.append('\n{}'.format(v_row.strip()))

    # creating the horizontal rows
    for i in range(2):
        if i % 2 == 0:
            word_ = word
        else:
            word_ = word[::-1]
        h_row = '{}'.format(word_[0])
        for j in range(width):
            if j % 2 == 0:
                h_row += ' {}'.format(' '.join(word_[1:]))
            else:
                h_row += ' {}'.format(' '.join(word_[:-1][::-1]))
        h_rows.append(h_row)

    for k in range(height):
        if k % 2 == 0:
            v_rows_ = v_rows
        else:
            v_rows_ = v_rows[::-1]

        final_reckt += '{}{}\n'.format(h_rows[k % 2], ''.join(v_rows_))
    final_reckt += h_rows[height % 2]  # add bottom row

    return '\n{}\n'.format(final_reckt)

if __name__ == '__main__':
    while True:
        try:
            word = input('Enter a word (leave blank to quit): ')
            if word == '':
                break
            width = int(input('Enter width of rectangle: '))
            height = int(input('Enter height of rectangle: '))
            print(recktangle(word, width, height))
        except ValueError:
            print('Invalid input. Try again.')

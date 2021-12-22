filename = 'day20/input.txt'
with open(filename, 'r') as f:
    contents = f.read().split('\n\n')

contents = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###""".split('\n\n')

algo = contents[0]
image = contents[1].split('\n')
for line in image:
    print(line)

print(len(line), len(image))

print(len(algo))

pixels = {}
for y, line in enumerate(image):
    for x, pixel in enumerate(line):
        pixels[(x, y)] = pixel

print(pixels)
print(len(pixels))

def binary_decoder(binary):
    binary = binary[::-1]
    value = 0
    bit_value = 1
    for bit in binary:
        if bit == '#':
            value += bit_value
        bit *= 2
    return value

def pixel_mapper(x, y):
    global pixels
    global algo
    binary = ''
    for y in range(y - 1, y + 2):
        for x in range(x - 1, x + 2):
            try:
                binary += pixels[(x, y)]
            except KeyError:
                # pixels[(x, y)] = '.'
                binary += '.'
    return algo[binary_decoder(binary)]

for pixel in pixels:
    pixels[pixel] = pixel_mapper(*pixel)

print(pixels)
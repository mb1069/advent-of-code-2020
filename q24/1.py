from q24.shared import read_file, TileWalk


def main():
    black_tiles = set()
    tpaths = read_file()
    black_to_white = 0
    white_to_black = 0
    for tpath in tpaths:
        coords = TileWalk(tpath).find_tile()
        if coords in black_tiles:
            black_tiles.remove(coords)
            black_to_white += 1
        else:
            black_tiles.add(coords)
            white_to_black += 1
    print(len(black_tiles))
    return black_tiles


if __name__ == '__main__':
    main()

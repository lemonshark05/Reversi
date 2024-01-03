# α-β search & ai player *Reversi*


## Requirement
- `brew install pkg-config`
- `brew install alexreg/dev/rocksdb@6`
- `brew install snappy`

export LIBRARY_PATH="$LIBRARY_PATH:/opt/homebrew/lib/"
echo $LIBRARY_PATH
g++  *.cpp -o noninteractive -std=c++17 -DFIND_FROM_DB -DNOINTERACTIVE $flag -DCLI -DTEST `pkg-config --cflags --libs protobuf` -I/opt/homebrew/opt/rocksdb@6/include -lsnappy -lgflags -lz -lbz2 -llz4 -lzstd /opt/homebrew/opt/rocksdb@6/lib/librocksdb.a

## Reversi (Othello) Board Representation
In Reversi, the board consists of an 8x8 grid, and each cell can be either empty, black, or white. To represent the board, you can use a 2D array in JavaScript. In this array, you can use numeric values to denote the different states:

<img width="557" alt="Reversi" src="https://github.com/lemonshark05/Reversi/assets/100770743/24548d1f-266e-4cb0-8781-5a010643fcee">

0 for empty cells.
1 for black pieces.
-1 for white pieces.
For example:
```
const reversiBoard = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 0, -1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
];
```
* Move History Tracking
To track the move history, you can use a JavaScript array. Each element of the array represents a move, and you can store the positions as strings in the format "d5" or "e4." Additionally, you can use another array to store the corresponding player colors ("b" for black, "w" for white).
* JavaScritp Map
To use a Map(in JavaScritp, the map is ordered) to track move history and then convert it to a string in the format "d5b_d4w_e4b_e5w". The Map stores each move's position as the key (e.g., "d5") and the player color (either "b" for black or "w" for white) as the value. After each move, the code will convert this Map into the string format.

## Development Guide to solve an board
1. encode your board by string,
for example: for ![](./opennings/pu_yue.png), you need to encode it to h8_i9,
this is the board to solve,
, and last black move is c5, this is guided move
- board to solve: d5_d4_e4_e5_d3
- guided move: c3

2. solve your board with guided move
```bash
./problem_comb.sh d5_d4_e4_e5_d3 c3
```

during the time, in order to see more debug info, run
```bash
tail -f reversi/script/run.py.log
```

cd reversi
./noninteractive

export PATH="/opt/homebrew/opt/rocksdb/bin:$PATH"
export LDFLAGS="-L/opt/homebrew/opt/rocksdb/lib"
export CPPFLAGS="-I/opt/homebrew/opt/rocksdb/include"
export PKG_CONFIG_PATH="/opt/homebrew/opt/rocksdb/lib/pkgconfig"

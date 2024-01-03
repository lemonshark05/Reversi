# Reversi
Reversi ai

- `brew install pkg-config`
- `brew install alexreg/dev/rocksdb@6`
- `brew install snappy`

export LIBRARY_PATH="$LIBRARY_PATH:/opt/homebrew/lib/"
echo $LIBRARY_PATH
g++  *.cpp -o noninteractive -std=c++17 -DFIND_FROM_DB -DNOINTERACTIVE $flag -DCLI -DTEST `pkg-config --cflags --libs protobuf` -I/opt/homebrew/opt/rocksdb@6/include -lsnappy -lgflags -lz -lbz2 -llz4 -lzstd /opt/homebrew/opt/rocksdb@6/lib/librocksdb.a

# Development Guide to solve an board
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
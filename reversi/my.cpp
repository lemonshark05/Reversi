#include <iostream>
#include <bitset>

class ReversiBitboard {
public:
    ReversiBitboard() {
        // Initialize the board with the standard starting position
        white = 0x0000001008000000ULL;
        black = 0x0000000810000000ULL;
    }

    void setBit(unsigned long long &bitboard, int position) {
        bitboard |= 1ULL << position;
    }

    void clearBit(unsigned long long &bitboard, int position) {
        bitboard &= ~(1ULL << position);
    }

    void flipBit(int position) {
        if (isBitSet(white, position)) {
            clearBit(white, position);
            setBit(black, position);
        } else if (isBitSet(black, position)) {
            clearBit(black, position);
            setBit(white, position);
        }
    }

    bool isBitSet(unsigned long long bitboard, int position) const {
        return (bitboard & (1ULL << position)) != 0;
    }

    void printBoard() const {
        for (int row = 7; row >= 0; --row) {
            for (int col = 0; col < 8; ++col) {
                int pos = row * 8 + col;
                if (isBitSet(white, pos)) {
                    std::cout << "W ";
                } else if (isBitSet(black, pos)) {
                    std::cout << "B ";
                } else {
                    std::cout << ". ";
                }
            }
            std::cout << std::endl;
        }
    }

private:
    unsigned long long white, black;
};

int main() {
    ReversiBitboard board;
    board.printBoard();

    // Example: flipping a piece at position 27 (row 3, column 3)
    board.flipBit(27);
    std::cout << "\nAfter flipping position 27:" << std::endl;
    board.printBoard();

    return 0;
}

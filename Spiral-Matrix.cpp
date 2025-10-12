#include <iostream>
#include <vector>

void printSpiral(const std::vector<std::vector<int>>& matrix) {
    if (matrix.empty() || matrix[0].empty()) {
        return; // Handle empty matrix
    }

    int rows = matrix.size();
    int cols = matrix[0].size();

    int top = 0;
    int bottom = rows - 1;
    int left = 0;
    int right = cols - 1;

    while (top <= bottom && left <= right) {
        // Traverse right (top row)
        for (int i = left; i <= right; ++i) {
            std::cout << matrix[top][i] << " ";
        }
        top++;

        // Traverse down (rightmost column)
        for (int i = top; i <= bottom; ++i) {
            std::cout << matrix[i][right] << " ";
        }
        right--;

        // Traverse left (bottom row), if applicable
        if (top <= bottom) {
            for (int i = right; i >= left; --i) {
                std::cout << matrix[bottom][i] << " ";
            }
            bottom--;
        }

        // Traverse up (leftmost column), if applicable
        if (left <= right) {
            for (int i = bottom; i >= top; --i) {
                std::cout << matrix[i][left] << " ";
            }
            left++;
        }
    }
    std::cout << std::endl;
}

int main() {
    std::vector<std::vector<int>> matrix1 = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    std::vector<std::vector<int>> matrix2 = {
        {1, 2, 3},
        {8, 9, 4},
        {7, 6, 5}
    };

    std::cout << "Spiral order for matrix 1: ";
    printSpiral(matrix1);

    std::cout << "Spiral order for matrix 2: ";
    printSpiral(matrix2);

    return 0;
}

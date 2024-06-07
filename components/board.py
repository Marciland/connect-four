'''component class for managing the board.'''
from .cell import Cell
from .entry_point import EntryPoint


class Board:
    '''Board component for the connect four game.'''

    def __init__(self, window) -> None:
        self.window = window
        self.rows = 6
        self.cols = 7
        self.entry_points = {}
        self.cells = {}

        self._prepare_board()

    def _prepare_board(self) -> None:
        '''Creates an empty board by placing all necessary widgets.'''
        for col_index in range(0, self.cols, 1):
            entry_point = EntryPoint(self.window, col_index)
            self.entry_points.update({col_index: entry_point})
            for row_index in range(0, self.rows, 1):
                cell = Cell(self.window, col_index, row_index)
                self.cells.update({
                    f'{col_index}x{row_index}': cell
                })

    def is_full(self) -> bool:
        '''True if no cell is empty.'''
        for _, cell in self.cells.items():
            if cell.is_empty():
                return False
        return True

    def connected_four(self) -> bool:
        '''True if the board has 4 connected of the same color anywhere.'''
        if self._vertical_connected_four():
            return True
        if self._horizontal_connected_four():
            return True
        if self._diagonal_connected_four():
            return True
        return False

    def _has_4_connected(self, cells: list[Cell]) -> bool:
        '''True if the list contains 4 of the same state neighbouring.'''
        connected = 0
        player = 0
        for cell in cells:
            if connected == 4:
                return True
            if cell.is_empty():
                connected = 0
                continue
            if player == cell.current_player:
                connected += 1
                continue
            player = cell.current_player
            connected = 1
        if connected == 4:
            return True
        return False

    def _vertical_connected_four(self) -> bool:
        '''True if 4 of the same color are vertically connected'''
        cells_by_col = [self._get_cells_in_col(col_index) for col_index
                        in range(0, self.rows)]
        for col in cells_by_col:
            if self._has_4_connected(col):
                return True
        return False

    def _get_cells_in_col(self, col: int) -> list[Cell]:
        '''Creates a list of all cells in the given col.'''
        return [cell for pos, cell in self.cells.items() if f'{col}x' in pos]

    def _horizontal_connected_four(self) -> bool:
        '''True if 4 of the same color are horizontally connected'''
        cells_by_row = [self._get_cells_in_row(row_index) for row_index
                        in range(0, self.cols)]
        for row in cells_by_row:
            if self._has_4_connected(row):
                return True
        return False

    def _get_cells_in_row(self, row: int) -> list[Cell]:
        '''Creates a list of all cells in the given row.'''
        return [cell for pos, cell in self.cells.items() if f'x{row}' in pos]

    def _diagonal_connected_four(self) -> bool:
        '''True if 4 of the same color are diagonally connected'''
        for up_diagonal in self._get_rising_diagonals():
            if self._has_4_connected(up_diagonal):
                return True
        for down_diagonal in self._get_falling_diagonal():
            if self._has_4_connected(down_diagonal):
                return True
        return False

    def _get_rising_diagonals(self) -> list[list[Cell]]:
        '''Collect a list of all diagonals going up.'''
        def __get_rising_diagonal(col: int, row: int,
                                  diag: list[Cell] = None) -> list[Cell]:
            '''Helper for recursively stepping through the matrix.'''
            if diag is None:
                # dangerous default value
                diag = []
            # go right and up (rising)
            col_right = col + 1
            if col_right > self.cols:
                return diag
            row_above = row - 1
            if row_above < 0:
                return diag
            diag.append(self.cells[f'{col}x{row}'])
            return __get_rising_diagonal(col_right, row_above, diag)

        rising_diags = []
        for col in range(0, self.cols, 1):
            for row in range(0, self.rows, 1):
                diag = __get_rising_diagonal(col, row)
                # only 4 or more cells are important for winning
                if len(diag) >= 4:
                    rising_diags.append(diag)
        return rising_diags

    def _get_falling_diagonal(self) -> list[list[Cell]]:
        '''Collect a list of all diagonals going down.'''
        def __get_falling_diagonal(col: int, row: int,
                                   diag: list[Cell] = None) -> list[Cell]:
            '''Helper for recursively stepping through the matrix.'''
            if diag is None:
                # dangerous default value
                diag = []
            # go right and down (falling)
            col_right = col + 1
            if col_right > self.cols:
                return diag
            row_below = row + 1
            if row_below > self.rows:
                return diag
            diag.append(self.cells[f'{col}x{row}'])
            return __get_falling_diagonal(col_right, row_below, diag)

        falling_diags = []
        for col in range(0, self.cols, 1):
            for row in range(0, self.rows, 1):
                diag = __get_falling_diagonal(col, row)
                if len(diag) >= 4:
                    falling_diags.append(diag)
        return falling_diags

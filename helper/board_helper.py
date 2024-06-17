'''Collection of board manipulating functions.'''
from assets import Cell, Position


def board_is_full(board_cells: dict[Position, Cell]) -> bool:
    '''True if no cell is empty.'''
    for _, cell in board_cells.items():
        if cell.is_empty():
            return False
    return True


def has_empty_cell(cells: list[Cell]) -> bool:
    '''True if no cell is empty.'''
    for cell in cells:
        if cell.is_empty():
            return True
    return False


def get_cells_in_col(board_cells: dict[Position, Cell], col: int) -> list[Cell]:
    '''Creates a list of all cells in the given col.'''
    return [cell for pos, cell in board_cells.items() if pos.x == col]


def get_cells_in_row(board_cells:  dict[Position, Cell], row: int) -> list[Cell]:
    '''Creates a list of all cells in the given row.'''
    return [cell for pos, cell in board_cells.items() if pos.y == row]


def has_connected_four(board_cells:  dict[Position, Cell], cols: int, rows: int) -> bool:
    '''True if the board has 4 connected of the same color anywhere.'''
    if _has_vertically_connected(board_cells=board_cells,
                                 cols=cols):
        return True
    if _has_horizontally_connected(board_cells=board_cells,
                                   rows=rows):
        return True
    if _diagonal_connected_four(board_cells=board_cells,
                                rows=rows,
                                cols=cols):
        return True
    return False


def _has_4_connected(cells: list[Cell]) -> bool:
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


def _has_vertically_connected(board_cells:  dict[Position, Cell], cols: int) -> bool:
    '''True if 4 of the same color are vertically connected'''
    cells_by_col = [get_cells_in_col(board_cells=board_cells,
                                     col=col_index)
                    for col_index
                    in range(0, cols)]
    for col in cells_by_col:
        if _has_4_connected(col):
            return True
    return False


def _has_horizontally_connected(board_cells:  dict[Position, Cell], rows: int) -> bool:
    '''True if 4 of the same color are horizontally connected'''
    cells_by_row = [get_cells_in_row(board_cells=board_cells,
                                     row=row_index)
                    for row_index
                    in range(0, rows)]
    for row in cells_by_row:
        if _has_4_connected(row):
            return True
    return False


def _diagonal_connected_four(board_cells:  dict[Position, Cell], cols: int, rows: int) -> bool:
    '''True if 4 of the same color are diagonally connected'''
    diagonals = _get_falling_diagonal(board_cells=board_cells,
                                      rows=rows,
                                      cols=cols) + \
        _get_rising_diagonals(board_cells=board_cells,
                              rows=rows,
                              cols=cols)
    for diagonal in diagonals:
        if _has_4_connected(diagonal):
            return True
    return False


def _get_rising_diagonals(board_cells:  dict[Position, Cell],
                          cols: int,
                          rows: int) -> list[list[Cell]]:
    '''Collect a list of all diagonals going up.'''
    def __get_rising_diagonal(col: int, row: int,
                              diag: list[Cell] = None) -> list[Cell]:
        '''Helper for recursively stepping through the matrix.'''
        if diag is None:
            # dangerous default value
            diag = []
        current_position = Position(x=col, y=row)
        diag.append(board_cells[current_position])
        next_position = current_position.add(Position(x=1, y=-1))
        if next_position.x > cols - 1:
            return diag
        if next_position.y < 0:
            return diag
        return __get_rising_diagonal(next_position.x, next_position.y, diag)

    rising_diags = []
    for col in range(0, cols, 1):
        for row in range(0, rows, 1):
            diag = __get_rising_diagonal(col, row)
            # only 4 or more cells are important for winning
            if len(diag) >= 4:
                rising_diags.append(diag)
    return rising_diags


def _get_falling_diagonal(board_cells:  dict[Position, Cell],
                          cols: int,
                          rows: int) -> list[list[Cell]]:
    '''Collect a list of all diagonals going down.'''
    def __get_falling_diagonal(col: int, row: int,
                               diag: list[Cell] = None) -> list[Cell]:
        '''Helper for recursively stepping through the matrix.'''
        if diag is None:
            # dangerous default value
            diag = []
        current_position = Position(x=col, y=row)
        diag.append(board_cells[current_position])
        next_position = current_position.add(Position(x=1, y=1))
        if next_position.x > cols - 1:
            return diag
        if next_position.y > rows - 1:
            return diag
        return __get_falling_diagonal(next_position.x, next_position.y, diag)

    falling_diags = []
    for col in range(0, cols, 1):
        for row in range(0, rows, 1):
            diag = __get_falling_diagonal(col, row)
            if len(diag) >= 4:
                falling_diags.append(diag)
    return falling_diags

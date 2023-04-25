import chess_engine
import Piece
from unittest.mock import patch, Mock, MagicMock


def test_knight_get_valid_peaceful_moves():
    """
    Unit tests for the get_valid_peaceful_moves method of the Knight class
    """

    # global instance of the game_state
    my_game_state = chess_engine.game_state()

    # =============== Boundary Values Test 01 ==================

    # configure the game_state
    my_game_state.board = [[chess_engine.Player.EMPTY] * 8 for _ in range(8)]
    my_game_state.board[3][4] = Piece.Knight('k', 3, 4, chess_engine.Player.PLAYER_1)
    my_game_state.white_pieces = [my_game_state.board[3][4]]
    my_game_state.black_pieces = []

    # T01 - Knight is in the center of the board without any another pieces in the board
    result = my_game_state.white_pieces[0].get_valid_peaceful_moves(my_game_state)
    expected_result = [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 5), (5, 3)]
    assert result == expected_result

    # =============== Boundary Values Test 02 ==================

    # reconfigure the game_state
    my_game_state.board = [[chess_engine.Player.EMPTY] * 8 for _ in range(8)]
    my_game_state.board[0][1] = Piece.Knight('k', 0, 1, chess_engine.Player.PLAYER_1)
    my_game_state.white_pieces = [my_game_state.board[0][1]]

    # T02 - Knight is in the left up corner (0,1) of the board without any another pieces in the board
    result = my_game_state.white_pieces[0].get_valid_peaceful_moves(my_game_state)
    expected_result = [(1, 3), (2, 2), (2, 0)]
    assert result == expected_result

    # =============== Boundary Values Test 03 ==================

    # configure the game_state
    my_game_state.board = [[chess_engine.Player.EMPTY] * 8 for _ in range(8)]
    my_game_state.board[1][3] = Piece.Knight('k', 1, 3, chess_engine.Player.PLAYER_1)
    my_game_state.board[0][1] = Piece.Pawn('p', 0, 1, chess_engine.Player.PLAYER_2)
    my_game_state.board[0][5] = Piece.Pawn('p', 0, 5, chess_engine.Player.PLAYER_2)
    my_game_state.board[2][1] = Piece.Pawn('p', 2, 1, chess_engine.Player.PLAYER_2)
    my_game_state.board[2][5] = Piece.Pawn('p', 2, 5, chess_engine.Player.PLAYER_2)
    my_game_state.board[3][4] = Piece.Pawn('p', 3, 4, chess_engine.Player.PLAYER_2)
    my_game_state.board[3][2] = Piece.Pawn('p', 3, 2, chess_engine.Player.PLAYER_2)

    my_game_state.white_pieces = [my_game_state.board[1][3]]
    my_game_state.black_pieces = [my_game_state.board[0][1], my_game_state.board[0][5], my_game_state.board[2][1],
                                  my_game_state.board[2][5], my_game_state.board[3][4], my_game_state.board[3][2]]

    # T03 - Knight is in a random place of the board with no valid peaceful moves
    result = my_game_state.white_pieces[0].get_valid_peaceful_moves(my_game_state)
    expected_result = []
    assert result == expected_result


def test_knight_get_valid_piece_takes():
    """
    Unit tests for the get_valid_piece_takes method of the Knight class
    """

    # global instance of the game_state
    my_game_state = chess_engine.game_state()

    # =============== Boundary Values Test 01 ==================

    # configure the game_state
    my_game_state.board = [[chess_engine.Player.EMPTY] * 8 for _ in range(8)]
    my_game_state.board[3][4] = Piece.Knight('k', 3, 4, chess_engine.Player.PLAYER_1)
    my_game_state.white_pieces = [my_game_state.board[3][4]]
    my_game_state.black_pieces = []

    # T01 - There is not valid pieces to take
    result = my_game_state.white_pieces[0].get_valid_piece_takes(my_game_state)
    expected_result = []
    assert result == expected_result

    # =============== Boundary Values Test 02 ==================

    # configure the game_state
    my_game_state.board = [[chess_engine.Player.EMPTY] * 8 for _ in range(8)]
    my_game_state.board[3][4] = Piece.Knight('k', 3, 4, chess_engine.Player.PLAYER_1)
    my_game_state.board[1][3] = Piece.Pawn('p', 1, 3, chess_engine.Player.PLAYER_2)
    my_game_state.board[1][5] = Piece.Pawn('p', 1, 5, chess_engine.Player.PLAYER_2)
    my_game_state.board[2][2] = Piece.Pawn('p', 2, 2, chess_engine.Player.PLAYER_2)
    my_game_state.board[2][6] = Piece.Pawn('p', 2, 6, chess_engine.Player.PLAYER_2)
    my_game_state.board[4][2] = Piece.Pawn('p', 4, 2, chess_engine.Player.PLAYER_2)
    my_game_state.board[4][6] = Piece.Pawn('p', 4, 6, chess_engine.Player.PLAYER_2)
    my_game_state.board[5][5] = Piece.Pawn('p', 5, 5, chess_engine.Player.PLAYER_2)
    my_game_state.board[5][3] = Piece.Pawn('p', 5, 3, chess_engine.Player.PLAYER_2)

    my_game_state.white_pieces = [my_game_state.board[3][4]]
    my_game_state.black_pieces = [my_game_state.board[1][3], my_game_state.board[1][5], my_game_state.board[2][2],
                                  my_game_state.board[2][6], my_game_state.board[4][2], my_game_state.board[4][6],
                                  my_game_state.board[5][5], my_game_state.board[5][3]]

    # T02 - maximum pieces to take (8)
    result = my_game_state.white_pieces[0].get_valid_piece_takes(my_game_state)
    expected_result = [(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 5), (5, 3)]
    assert result == expected_result

    # =============== Boundary Values Test 03 ==================

    # configure the game_state
    my_game_state.board = [[chess_engine.Player.EMPTY] * 8 for _ in range(8)]
    my_game_state.board[3][4] = Piece.Knight('k', 3, 4, chess_engine.Player.PLAYER_1)
    my_game_state.board[1][3] = Piece.Pawn('p', 1, 3, chess_engine.Player.PLAYER_2)
    my_game_state.board[1][5] = Piece.Pawn('p', 1, 5, chess_engine.Player.PLAYER_2)
    my_game_state.board[2][2] = Piece.Pawn('p', 2, 2, chess_engine.Player.PLAYER_2)
    my_game_state.board[2][6] = Piece.Pawn('p', 2, 6, chess_engine.Player.PLAYER_2)
    my_game_state.board[4][2] = Piece.Pawn('p', 4, 2, chess_engine.Player.PLAYER_1)
    my_game_state.board[4][6] = Piece.Pawn('p', 4, 6, chess_engine.Player.PLAYER_1)
    my_game_state.board[5][5] = Piece.Pawn('p', 5, 5, chess_engine.Player.PLAYER_1)
    my_game_state.board[5][3] = Piece.Pawn('p', 5, 3, chess_engine.Player.PLAYER_1)

    my_game_state.white_pieces = [my_game_state.board[3][4], my_game_state.board[4][2], my_game_state.board[4][6],
                                  my_game_state.board[5][5], my_game_state.board[5][3]]
    my_game_state.black_pieces = [my_game_state.board[1][3], my_game_state.board[1][5], my_game_state.board[2][2],
                                  my_game_state.board[2][6]]

    # T03 - some pieces to take are from the current player, and some note
    result = my_game_state.white_pieces[0].get_valid_piece_takes(my_game_state)
    expected_result = [(1, 3), (1, 5), (2, 2), (2, 6)]
    assert result == expected_result

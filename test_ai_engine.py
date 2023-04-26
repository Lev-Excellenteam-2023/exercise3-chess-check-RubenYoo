import chess_engine
import ai_engine
import Piece
from unittest.mock import patch


def test_evaluate_board():
    """
    Integration test for the evaluate_board method of the ai_engine class
    """

    # creating a chess_ai instance
    my_ai_engine = ai_engine.chess_ai()

    # configuring the board
    my_game_state = chess_engine.game_state()

    # configure the patch
    patched_board = [[chess_engine.Player.EMPTY] * 8 for _ in range(8)]
    patched_board[3][4] = Piece.Pawn('p', 3, 4, chess_engine.Player.PLAYER_1)

    with patch.object(my_game_state, 'board', patched_board):
        expected_result = 10
        result = my_ai_engine.evaluate_board(my_game_state, chess_engine.Player.PLAYER_2)

        # T01 - basic evaluate_board test
        assert result == expected_result


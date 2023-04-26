import chess_engine


def test_fool_s_mate():
    """
    System test
    """

    # configuring the game_state
    my_game_state = chess_engine.game_state()

    # make the moves for the fool's mate
    my_game_state.move_piece((1, 2), (2, 2), False)
    my_game_state.move_piece((6, 3), (5, 3), False)
    my_game_state.move_piece((1, 1), (3, 1), False)
    my_game_state.move_piece((7, 4), (3, 0), False)

    expected_result = 0
    result = my_game_state.checkmate_stalemate_checker()
    
    # T01 - is white lost ?
    assert result == expected_result

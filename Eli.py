from copy import deepcopy
from constants import RED, WHITE, ROWS, COLS
import random


class Eli:
    @staticmethod
    def minimax(current_board, depth, max_player):
        if depth == 0 or current_board.winner(RED) or current_board.winner(WHITE):
            return Eli.evaluate_algorithm(current_board), current_board

        if max_player:
            max_eval = float('-inf')
            best_move = None
            for move in Eli.get_all_moves(current_board, WHITE):
                evaluation = Eli.minimax(move, depth - 1, False)[0]
                max_eval = max(max_eval, evaluation)
                if max_eval == evaluation:
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in Eli.get_all_moves(current_board, RED):
                evaluation = Eli.minimax(move, depth - 1, True)[0]
                min_eval = min(min_eval, evaluation)
                if min_eval == evaluation:
                    best_move = move
            return min_eval, best_move

    @staticmethod
    def get_all_moves(board, color):
        moves = []
        possible_moves = board.get_valid_moves()
        for column in range(len(possible_moves)):
            if possible_moves[column] != -1:
                temp_board = deepcopy(board)
                temp_board.add_piece(color, column)
                moves.append(temp_board)

        if board.winner(RED) or board.winner(WHITE):
            return []

        return moves

    @staticmethod
    def evaluate_algorithm(board):
        return Eli.total_score(WHITE, board) - Eli.total_score(RED, board)

    @staticmethod
    def total_score(color, board):
        score = 0
        vert_count = 0

        # vertical combos
        vert_count = 0
        for column in range(COLS):
            for row in range(ROWS):
                if board[row][column] != 0 and board[row][column].color == color:
                    vert_count += 1
                else:
                    vert_count = 0

        if vert_count == 0:
            score += 1
        elif vert_count == 1:
            score += 2
        elif vert_count == 2:
            score += 3

        # horizontal combos
        hori_count = 0
        for column in range(COLS):
            for row in range(ROWS):
                if board[row][column] != 0 and board[row][column].color == color:
                    hori_count += 1
                else:
                    hori_count = 0

        if hori_count == 0:
            score += 1
        elif hori_count == 1:
            score += 2
        elif hori_count == 2:
            score += 3

    # diagonal combos
        diag_count = 0
        diag_score = 0

        # diagonal down
        for row in range(3):
            for column in range(4):
                while diag_count < 4 and board[row + diag_count][column + diag_count] != 0 and board[row + diag_count][
                    column + diag_count].color == color:
                    diag_count += 1

        if diag_count == 0:
            diag_score += 1
        elif diag_count == 1:
            diag_score += 2
        elif diag_count == 2:
            diag_score += 3

        diag_count = 0





        # diagonal up
        for row in range(3):
            for column in range(4):
                while diag_count < 4 and board[row + diag_count][6 - column - diag_count] != 0 and \
                        board[row + diag_count][6 - column - diag_count].color == color:
                    diag_count += 1

        if diag_count == 0:
            diag_score += 1
        elif diag_count == 1:
            diag_score += 2
        elif diag_count == 2:
            diag_score += 3

        score += diag_score





        return score
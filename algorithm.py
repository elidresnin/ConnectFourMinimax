from copy import deepcopy
from constants import RED, WHITE
import random


class Algorithm:
    @staticmethod
    def minimax(current_board, depth, max_player):
        if depth == 0 or current_board.winner(RED) or current_board.winner(WHITE):
            return Algorithm.evaluate_algorithm(current_board), current_board

        if max_player:
            max_eval = float('-inf')
            best_move = None
            for move in Algorithm.get_all_moves(current_board, WHITE):
                evaluation = Algorithm.minimax(move, depth - 1, False)[0]
                max_eval = max(max_eval, evaluation)
                if max_eval == evaluation:
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in Algorithm.get_all_moves(current_board, RED):
                evaluation = Algorithm.minimax(move, depth - 1, True)[0]
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
        return Algorithm.total_score(WHITE, board) - Algorithm.total_score(RED, board)

    @staticmethod
    def total_score(color, board):
        return random.randint(1, 10)
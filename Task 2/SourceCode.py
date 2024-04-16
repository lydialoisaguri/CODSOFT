class TicTacToe:
  def __init__(self):
    self.current_player = "X"
    self.board = [" " for _ in range(9)]

  def print_board(self):
    for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
      print(' | ' + ' | '.join(row) + ' | ')
      print(' ')

  def make_move(self, position):
    if self.board[position] == ' ':
      self.board[position] = self.current_player
      if self.check_winner(self.current_player):
        print(f'{self.current_player} wins!')
        return True
      elif ' ' not in self.board:
        print("It's a draw!")
        return True
      self.current_player = 'O' if self.current_player == 'X' else 'X'
    else:
      print('Invalid move. Try again.')
    return False

  def check_winner(self, player):
    for i in range(3):
      if self.board[i] == self.board[i+3] == self.board[i+6] == player:
        return True
      if self.board[i*3] == self.board[i*3+1] == self.board[i*3+2] == player:
        return True
    if self.board[0] == self.board[4] == self.board[8] == player:
      return True
    if self.board[2] == self.board[4] == self.board[6] == player:
      return True
    return False

  def minimax(self, depth, is_maximizing):
    if self.check_winner('X'):
      return -1
    elif self.check_winner('O'):
      return 1
    elif ' ' not in self.board:
      return 0

    if is_maximizing:
      best_score = -float('inf')
      for i in range(9):
        if self.board[i] == ' ':
          self.board[i] = 'O'
          score = self.minimax(depth + 1, False)
          self.board[i] = ' '
          best_score = max(score, best_score)
      return best_score
    else:
      best_score = float('inf')
      for i in range(9):
        if self.board[i] == ' ':
          self.board[i] = 'X'
          score = self.minimax(depth + 1, True)
          self.board[i] = ' '
          best_score = min(score, best_score)
      return best_score

  def play_game(self):
    while True:
      self.print_board()
      if self.current_player == 'X':
        move = int(input(f"Player {game.current_player}, Enter your move (0-8):"))
      else:
        best_score = -float('inf')
        best_move = None
        for i in range(9):
          if self.board[i] == ' ':
            self.board[i] = 'O'
            score = game.minimax(0, False)
            self.board[i] = ' '
            if score > best_score:
              best_score = score
              best_move = i
        move = best_move

      if self.make_move(move):
        break
# Cteate an instance of TicTacToe and start the game
game = TicTacToe()
game.play_game()

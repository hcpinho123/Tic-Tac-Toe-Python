''' Henrique Pinho
- Title of the program: Tic-Tac-Toe
- This program is created to make a Tic Tac Toe game in the computer 
- sources: https://doc.qt.io/qtforpython-6/
- first drfat: 11/12/2023
- last modification: 11/15/2023
- note: the winner always start!
'''
import os 
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QPushButton, QMessageBox

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac_Toe")
        grid = QGridLayout()
        
        # create the game-layout
        self.board(grid)
           
        #gamelogic
        self.currentPlayer = 'x'
        self.xStyle = "color: blue; font-size: 80px;"
        self.OStyle = "color: red; font-size: 80px;"
        
        # count wins and restart
        self.restart = QPushButton("Restart")
        self.restart.clicked.connect(self.restart_game)
        grid.addWidget(self.restart, 3, 1)
        
        self.countxWin = 0
        self.countOWin = 0
        self.countTies = 0
        
        self.xwins = QLabel(f'Player x won {self.countxWin} games')
        self.Owins = QLabel(f'Player O won {self.countOWin} games')
        self.tiedGame = QLabel(f'Tied game(s): {self.countTies} ')
        grid.addWidget(self.xwins, 3, 0)
        grid.addWidget(self.Owins, 3, 2)
        grid.addWidget(self.tiedGame, 4, 1)

        # add layout to window
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)
        
    def board(self, grid):
        self.style = "width: 100px; height: 100px;"
        self.buttons = []

        for row in range(3):
            for column in range(3):
                button = QPushButton("")
                button.clicked.connect(self.click)
                button.setStyleSheet(self.style)
                grid.addWidget(button, row, column)
                self.buttons.append(button)
                
    def click(self, grid):
        button = self.sender()
        if button.text() == '':
            marker = self.currentPlayer
            style = self.xStyle if marker == 'x' else self.OStyle

            button.setText(marker)
            button.setStyleSheet(style)
            self.checkForWin()
            self.currentPlayer = 'x' if self.currentPlayer == 'O' else 'O'
    
    def checkForWin(self):
        """
        Check if a player has won and update the game state accordingly.

        This method is called after each move to check if there's a winner.

        >>> window = TicTacToe()

        >>> window.buttons[0].setText('x')
        >>> window.buttons[1].setText('x')
        >>> window.buttons[2].setText('x')
        >>> window.checkForWin()
        >>> window.xWon
        True
        
        >>> window.buttons[0].setText('x')
        >>> window.buttons[3].setText('x')
        >>> window.buttons[6].setText('x')
        >>> window.checkForWin()
        >>> window.xWon
        True
        
        >>> window.buttons[0].setText('x')
        >>> window.buttons[4].setText('x')
        >>> window.buttons[8].setText('x')
        >>> window.checkForWin()
        >>> window.xWon
        True
        """
        self.xWon = False
        self.OWon = False
        self.tied = False
        winstyleX = "background-color: lightgreen; width: 100px; height: 100px; color:blue; font-size: 80px;"
        winstyleO = "background-color: lightgreen; width: 100px; height: 100px; color:red; font-size: 80px;"
        winningCombinations =[[0, 1, 2], [3,4,5], [6,7,8], [0,4,8], [2,4,6], [0, 3, 6], [1,4,7], [2,5,8]]
        for win_check in winningCombinations:
            buttonNum1, buttonNum2, buttonNum3 = win_check
            if self.buttons[buttonNum1].text() == self.currentPlayer and self.buttons[buttonNum2].text() == self.currentPlayer and self.buttons[buttonNum3].text() == self.currentPlayer:
                if self.currentPlayer == 'x':
                    winstyle = winstyleX
                    self.xWon = True
                    self.countxWin += 1
                    self.xwins.setText(f'Player x won {self.countxWin} games')
                    
                elif self.currentPlayer == 'O':
                    winstyle = winstyleO
                    self.OWon = True
                    self.countOWin += 1
                    self.Owins.setText(f'Player O won {self.countOWin} games')
                
                self.buttons[buttonNum1].setStyleSheet(winstyle)
                self.buttons[buttonNum2].setStyleSheet(winstyle)
                self.buttons[buttonNum3].setStyleSheet(winstyle)
                
                for button in self.buttons:
                    button.setEnabled(False)

        # Check for a tie
        if all(button.text() for button in self.buttons) and not self.xWon and not self.OWon:
            self.tied = True
            self.countTies += 1
            self.tiedGame.setText(f'Tied game(s):{self.countTies} ')
            for button in self.buttons:
                button.setEnabled(False)
            
    def restart_game(self):
        if self.currentPlayer == 'x':
            self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'x'
        # Create a QMessageBox
        restart_confirmation = QMessageBox()
        restart_confirmation.setText("Are you sure you want to restart?!")
        restart_confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        
        # Get the user's response
        returnValue = restart_confirmation.exec()

        # Check the user's response
        if returnValue == QMessageBox.Yes:
            for button in self.buttons:
                button.setEnabled(True)
                button.setText('')
                button.setStyleSheet(self.style)
            
if __name__ == "__main__":
    app = QApplication()
    import doctest
    doctest.testmod()
    window = TicTacToe()
    window.show()
    app.exec()
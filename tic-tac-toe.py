

theBoard={'top-l':' ','top-m':' ','top-r':' ','mid-l':' ','mid-m':' ','mid-r':' ','low-l':' ','low-m':' ','low-r':' '}
print 'welcome! get ready to play tic-tac-toe'

print ("Refer the commands to position your tile in the board\n"
       "top-l | top-m |top-r\n"
       "------+-------+-----\n"
       "mid-l | mid-m |mid-r\n"
        "------+-------+-----\n"
       "low-l | low-m |low-r")


def printboard(board):
  print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'] + '\n'
  '-+-+-\n' + board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'] + '\n'
  '-+-+-\n' + board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'] + '\n')
 
   
print 'Enter your choice X or O '
choice =  raw_input()
print 'You have chosen '+choice
#printboard(theBoard);

for i in range(9):
    move=raw_input(choice + ' move to which place?')
    theBoard[move]=choice
    printboard(theBoard);
    if choice == 'X':
       choice = 'O'
    else:
       choice = 'X'



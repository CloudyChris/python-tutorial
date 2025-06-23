grid = '''##########
#& #     #
#  #     #
#X #     #
#      X@#
##########'''

wall = "#"
space = " "
player = "&"
goal = "@"
trap = "X"

class Character:
    x = -1
    y= -1
    is_gameover = False
    is_win = False
    grid_w = 0
    grid_h = 0
    comp_grid = []
    
    def main(self):
        self.setup()
        while not self.is_gameover:
            self.render()
            cmd = input("Move: ")
            if self.move(cmd):
                return True
                
    def setup(self):
        grid_arr = grid.split("\n")
        try:
            self.grid_h = len(grid_arr)
            self.grid_w = len(grid_arr[0])
        except:
            print("Grid bad")
        self.is_gameover = False
        self.is_win = False
        self.comp_grid = []
        for row in grid_arr:
            tmp_row = []
            for i in range(self.grid_w):
                tmp_row.append(row[i])
            self.comp_grid.append(tmp_row)

        for y in range(self.grid_h):
            for x in range(self.grid_w):
                if self.comp_grid[y][x] == player:
                    self.comp_grid[y][x] = space
                    self.x = x
                    self.y = y
                    return

    def _move(self, direction, amount):
        cx = self.x
        cy = self.y
        try:
            amount = int(amount)
        except:
            pass
        match direction:
            case "up":
               cy -= 1*amount
            case "down":
               cy += 1*amount
            case "left":
                cx -= 1*amount
            case "right":
                cx += 1*amount
            case "quit":
                self.is_gameover = True
                return self.end_game()
            case _:
                pass

        if cx >= 0 and cx <= self.grid_w and cy >= 0 and cy <= self.grid_h:
            if self.comp_grid[cy][cx] == wall:
                return False
            elif self.comp_grid[cy][cx] == trap:
                self.is_gameover = True
                return self.end_game()
            elif self.comp_grid[cy][cx] == goal:
                self.is_win = True
                self.is_gameover = True
                return self.end_game()
            
            self.x = cx
            self.y = cy
        
        return False
    
    def move(self, cmd):
        cmd = cmd.split(" ")

        move_cmd = ""
        move_amount = 1
        for token in cmd:
            if token == "quit":
                if self._move(token, move_amount):
                    return True
            if move_cmd != "":
                try:
                    move_amount = int(token)
                    self._move(move_cmd, move_amount)
                except:
                    if self._move(move_cmd, move_amount):
                        return True
            
            move_cmd = ""
            move_amount = 1

            if token in ["up", "down", "left", "right", "quit"]:
                move_cmd = token
        
        if move_cmd != "":
            if self._move(move_cmd, move_amount):
                return True
                
    def end_game(self):
        if self.is_win:
            print("##########")
            print("#        #")
            print("#   You  #")
            print("#  Win   #")
            print("#        #")
            print("##########")
        else:
            print("##########")
            print("#        #")
            print("#   You  #")
            print("#  Lose  #")
            print("#        #")
            print("##########")
        repl = ""
        while repl != "y" or repl != "n":
            repl = input("Play again(y/n)? ")
            if repl == "y":
                return True
            elif repl == "n":
                quit()
            else:
                print("Please answer y or n")
    
    def render(self):
        render_target = ""
        for y in range(self.grid_h):
            for x in range(self.grid_w):
                if self.x == x and self.y == y:
                    render_target += "&"
                else:
                    render_target += self.comp_grid[y][x]
            render_target += "\n"
    
        print(render_target)
        print("\n")

while True:
    character = Character()
    character.main()
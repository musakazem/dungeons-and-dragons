import os


from levels.tutorial import Tutorial
from world.generator import World
from world.render import Render
from mechanics.movement import Movement, positional_awareness
from universal.temporary_datas import coordinates
from db.tools import load_game
from universal.utils import clear_terminal
from logs.config import initiate_logs
    
def handle_triggers() -> None:

    if (player.x == level.info_trigger.x 
        and player.y == level.info_trigger.y):

        info = "The exit is in the room ahead. But watch your step!"
        info_2 = "Make sure to save your progress by using the 'S' station"
        info_all = info + info_2
        level.info_trigger.show_info(info_all)

    if (player.x == level.save_trigger.x
        and player.y == level.save_trigger.y):

        level.save_trigger.save_prompt(player.x, player.y + 1)



def handle_player_inputs(player_input: str) -> None:

    player_controller = Movement(player)

    input_options = positional_awareness(player, level.get_map)
    
    boundary_error = "You're going out of bounds!"

    if (player_input.lower() == "q"
        or player_input.lower() == "quit"):

        game_loop = False
        
    elif player_input.lower() == "right":

        if "RIGHT" in input_options:
            player_controller.move = "right"
            board.render_player(player)
        else:
            input(boundary_error)    
                
    elif player_input.lower() == "left":

        if "LEFT" in input_options:
            player_controller.move = "left"
            board.render_player(player)
        else:
            input(boundary_error)        

    elif player_input.lower() == "up":

        if "UP" in input_options:    
            player_controller.move = "up"
            board.render_player(player)
        else:
            input(boundary_error)

    elif player_input.lower() == "down":

        if "DOWN" in input_options:
            player_controller.move = "down"
            board.render_player(player)
        else:
            input(boundary_error)    


def game_object_permenance() -> None:
    """ Makes sure game object renders on the board again
        after player has overrided their place holders.
    """
    board.render_obj = level.info_trigger
    board.render_obj = level.save_trigger

logger = initiate_logs("main_logs")
logger.info("STARTED PROGRAM")
if __name__ == "__main__":


    run_once = 1

    program_running = True
    while program_running:
        game_loop = True
        menu = True
        if run_once == 1:
            level = Tutorial(18)
            player = level.player
            board = Render(level.get_map)
            run_once -= 1
        # board.render_map(0, 0 , 21) ->  for debugging

        while menu:

            clear_terminal()
            close = False

            if load_game() is None:
                    
                print("1. NEW GAME")

                print("Press 'Q' to quit")
                menu_input = input("Press 1 to continue... \n> ")
                
                if menu_input == "1":
                    player.x = 6
                    player.y = 12
                    board.render_obj = player
                    menu = close
                if menu_input == "q":
                    menu = close
                    program_running = False
                    game_loop = False

            else:
                print("1. NEW GAME")
                print("2. CONTINUE")

                print("Press 'Q' to quit")
                menu_input = input("Press 1 or 2 to continue... \n> ")

                if menu_input == "2":

                    load_x, load_y = load_game()
                    player.x = load_x
                    player.y = load_y
                    board.render_player(player)
                    menu = close

                elif menu_input == "1":
                    player.x = 6
                    player.y = 12
                    board.render_obj = player
                    menu = close
                elif menu_input.lower() == "q":
                    menu = close
                    program_running = False
                    game_loop = False
            
        while game_loop:

            clear_terminal()

            board.follow_player(player)

            game_object_permenance()

            handle_triggers()
            
            player_input = input("> ")
            handle_player_inputs(player_input)

            if (player_input.lower() == "q"
                or player_input.lower() == "quit"):

                game_loop = False
            
            if (player.x == level.dragon.x
                and player.y == level.dragon.y):

                end = input("** OH NO! The monster got you! Better luck next "
                            + "time! **")
                game_loop = False

            elif (player.x == level.gate.x
                and player.y == level.gate.y):

                end = input("** Congratulations, you made it out alive! **")
                game_loop = False


logger.info("ENDED PROGRAM")
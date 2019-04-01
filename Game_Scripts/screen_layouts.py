############################################################################
############################################################################

#Screen layouts
import Game_Scripts.ui_elements

ui_elements = Game_Scripts.ui_elements

############################################################################
############################################################################

screens = {



    'loading_screen' : {
        'ui_elements' : {
            'loading_label' : ui_elements.text_button(

                name = "loading_label",

                self_height=0.1,
                self_width=0.2,
                x_position=0.1,
                y_position=0.9,

                text="Loading",
                text_size=(0.08),
                text_color=(255,255,255),
                font=None,

                background_color=None,
                border_width=0,
                border_color=(0,0,0),

            ),
        },
    },



    'title_screen' : {
        'ui_elements' : {
            'bg' : ui_elements.image(

                name = "bg",

                self_height=1,
                self_width=1,
                x_position=0,
                y_position=0,

                image="Backgrounds/background.png",
                image_alpha=255,

            ),
            'duel_button' : ui_elements.text_button(

                name = "duel_button",

                self_height=0.1,
                self_width=0.2,
                x_position=0.9,
                y_position=0.6,

                text="Battle",
                text_size=(0.08),
                text_color=(255,255,255),
                font=None,

                background_color=(55,55,55),
                border_width=0,
                border_color=(0,0,0),
            ),
            'new_story_button' : ui_elements.text_button(

                name="new_story_button",

                self_height=0.1,
                self_width=0.2,
                x_position=0.9,
                y_position=0.35,

                text="New Game",
                text_size=(0.08),
                text_color=(255, 255, 255),
                font=None,

                background_color=(55, 55, 55),
                border_width=0,
                border_color=(0, 0, 0),
            ),
            'continue_story_button' : ui_elements.text_button(

                name="continue_story_button",

                self_height=0.1,
                self_width=0.2,
                x_position=0.9,
                y_position=0.475,

                text="Load Game",
                text_size=(0.08),
                text_color=(255, 255, 255),
                font=None,

                background_color=(55, 55, 55),
                border_width=0,
                border_color=(0, 0, 0),
            ),
            'settings_button' : ui_elements.text_button(

                name="settings_button",

                self_height=0.1,
                self_width=0.2,
                x_position=0.9,
                y_position=0.725,

                text="Settings",
                text_size=(0.08),
                text_color=(255, 255, 255),
                font=None,

                background_color=(55, 55, 55),
                border_width=0,
                border_color=(0, 0, 0),
            ),
            'quit_button' : ui_elements.text_button(

                name="quit_button",

                self_height=0.1,
                self_width=0.2,
                x_position=0.9,
                y_position=0.85,

                text="Quit",
                text_size=(0.08),
                text_color=(255, 255, 255),
                font=None,

                background_color=(55, 55, 55),
                border_width=0,
                border_color=(0, 0, 0),
            ),
        },
    },
}

############################################################################
############################################################################

def return_screen_elements(screen):

    for key in screens:

        if key == screen:

            ui_elements = []

            for element in screens[key]['ui_elements']:

                ui_elements.append(screens[key]['ui_elements'][element])

            return ui_elements
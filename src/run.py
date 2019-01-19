import wx
import pyautogui

def get_center(state):
    return state["x_pos"] + (state["width"]/2), state["y_pos"] + (state["height"] /2)


def get_initial_state():
    width, height = wx.GetDisplaySize()
    return {
        "height": height,
        "width": width,
        "x_pos": 0,
        "y_pos": 0
    }


def get_quadrants(state):
    return {
        1: {
            "height": state["height"] / 2,
            "width": state["width"] / 2,
            "x_pos": state["x_pos"] + state["width"] / 2,
            "y_pos": state["y_pos"]
        },
        2: {
            "height": state["height"] / 2,
            "width": state["width"] / 2,
            "x_pos": state["x_pos"],
            "y_pos": state["y_pos"]
        },
        3: {
            "height": state["height"] / 2,
            "width": state["width"] / 2,
            "x_pos": state["x_pos"],
            "y_pos": state["y_pos"] + state["height"] / 2
        },
        4: {
            "height": state["height"] / 2,
            "width": state["width"] / 2,
            "x_pos": state["x_pos"] + state["width"] / 2,
            "y_pos": state["y_pos"] + state["height"] / 2
        }
    }


def render(main_frame, state):
    main_frame.Show(False)

    if hasattr(main_frame, "panel1"):
        main_frame.panel1.Destroy()
        main_frame.panel2.Destroy()
        main_frame.panel3.Destroy()
        main_frame.panel4.Destroy()

    quadrants = get_quadrants(state)

    panel1 = Panel(main_frame, quadrants[1])
    panel2 = Panel(main_frame, quadrants[2])
    panel3 = Panel(main_frame, quadrants[3])
    panel4 = Panel(main_frame, quadrants[4])

    panel1.SetBackgroundColour ('red')
    panel2.SetBackgroundColour('yellow')
    panel3.SetBackgroundColour('green')
    panel4.SetBackgroundColour('blue')

    main_frame.panel1 = panel1
    main_frame.panel2 = panel2
    main_frame.panel3 = panel3
    main_frame.panel4 = panel4

    main_frame.ui_simulator.MouseMove(get_center(main_frame.state)[0], get_center(main_frame.state)[1])

    main_frame.Show()
    main_frame.Raise()


class Panel(wx.Panel):
    def __init__(self, parent, quadrant_props):
        super(Panel, self).__init__(parent, -1,
                                    pos=(quadrant_props["x_pos"], quadrant_props["y_pos"]),
                                    size=(quadrant_props["width"], quadrant_props["height"]))
        self.quadrant_props = quadrant_props

class MyFrame(wx.Frame):

    def __init__(self, parent, initial_state):
        wx.Frame.__init__(self, parent, -1, style=wx.BORDER_NONE)
        self.SetTransparent(100)
        self.SetSize(initial_state["width"], initial_state["height"])
        self.state = initial_state
        self.SetPosition((0, 0))

        self.ui_simulator = wx.UIActionSimulator()

        self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)

        self.register_hotkey()
        self.Bind(wx.EVT_HOTKEY, self.handle_hotkey, id=self.hotKeyId)



    def register_hotkey(self):
        self.hotKeyId = 100
        self.RegisterHotKey(self.hotKeyId, wx.MOD_SHIFT, ord('r'))

    def handle_hotkey(self, evt):
        self.state = get_initial_state()
        render(self, self.state)
        self.Raise()
        self.SetFocus()
        self.Show()

        print(self.FindFocus())
        print("hotkey pressed")


    def onKeyPress(self, event):
        keycode = event.GetKeyCode()
        print(keycode)
        key_code_to_quadrant = {73: 1, 69: 2, 70: 3, 74: 4}
        if keycode in key_code_to_quadrant.keys():
            new_state = get_quadrants(self.state)[key_code_to_quadrant[keycode]]
            self.state = new_state
            render(self, new_state)

        elif keycode == wx.WXK_SPACE:
            frame.Lower()
            frame.Hide()

            pyautogui.hotkey('command', 'tab')
            pyautogui.click(button="left")

            print("click")



if __name__ == '__main__':
    app = wx.App()
    initial_state = get_initial_state()
    frame = MyFrame(None, initial_state)
    frame.ShowFullScreen(True)
    render(frame, get_initial_state())
    app.MainLoop()
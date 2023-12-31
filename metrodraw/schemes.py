from abc import ABC, abstractmethod


class Scheme(ABC):
    @abstractmethod
    def get_basic_color(self, color_name):
        pass

    @abstractmethod
    def rcparams(self):
        pass

    def get_color(self, color_name):
        if color_name == "bg":
            return self.get_basic_color("white")
        if color_name == "fg":
            return self.get_basic_color("black")
        return self.get_basic_color(color_name)

    def modify_label(self, label):
        return label


class MBTA(Scheme):
    def get_basic_color(self, color_name):
        return {
            "red": "#e43037",
            "orange": "#f7941e",
            "yellow": "#fdd808",
            "green": "#009867",
            "blue": "#1b91d1",
            "purple": "#8c4799",
            "pink": "#e27ea6",
            "white": "#ffffff",
            "black": "#000000",
        }[color_name]

    def rcparams(self):
        return dict()

    def modify_label(self, label):
        return label.title()


class Retro(Scheme):
    def get_basic_color(self, color_name):
        return {
            "red": "#9c1f29",
            "orange": "#b62",
            "yellow": "#d8a71f",
            "green": "#395d39",
            "blue": "#3d447d",
            "purple": "#5d395d",
            "pink": "#d8a71f",
            "white": "#e8dacf",
            "black": "#000000",
        }[color_name]

    def rcparams(self):
        return {"font.family": "Futura"}

    def modify_label(self, label):
        return label.upper()


class Terminal(Scheme):
    def get_basic_color(self, color_name):
        return {
            "red": "#ff0000",
            "orange": "#ff8a00",
            "yellow": "#ffff00",
            "green": "#00ff00",
            "blue": "#0000ff",
            "purple": "#ff00ff",
            "pink": "#ff00ff",
            "white": "#000000",
            "black": "#ffffff",
        }[color_name]

    def rcparams(self):
        return {"font.family": "Courier New", "font.weight": "bold"}

    def modify_label(self, label):
        return label.lower()

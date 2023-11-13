from matplotlib import pyplot as plt
from metropy.model.coord import Coord
from metropy.utils.data_linewidth_plot import data_linewidth_plot


class Renderer:
    def __init__(self, dpi=200, lw=0.2, font_size=4, black="black", white="white"):
        self.fig = plt.figure(dpi=dpi, facecolor=white)
        self.ax = plt.gca()
        self.lw = lw
        self.font_size = font_size
        self.black = black
        self.white = white
        self._handles = []

    @property
    def coord_config(self):
        return dict(interlining_offset=self.lw)

    def line(self, line):
        for seg in line.segments:
            xs, ys = seg.coords(self.coord_config)
            self._handles += [
                data_linewidth_plot(
                    xs,
                    ys,
                    ax=self.ax,
                    linewidth=self.lw,
                    solid_capstyle="round",
                    # solid_joinstyle="miter",
                    color=line.color,
                )
            ]

    def station(self, station, no_label=False):
        # draw circle at station
        x, y = station.coord.get_x(self.coord_config), station.coord.get_y(
            self.coord_config
        )
        r = self.lw / 2
        for i, mark in enumerate(
            station.get_markers(x, y, r, black=self.black, white=self.white)
        ):
            # bring to front
            mark.zorder = 10 + i / 10
            self.ax.add_artist(mark)

        if not no_label:
            self.label(x, y, r, station.font_size, station.label)

    def interlining(self, coord, station):
        self.station(station.with_coord(coord), no_label=True)
        x1, y1 = station.coord.get_x(self.coord_config), station.coord.get_y(
            self.coord_config
        )
        x2, y2 = coord.get_x(self.coord_config), coord.get_y(self.coord_config)

        self._handles += [
            data_linewidth_plot(
                [x1, x2],
                [y1, y2],
                ax=self.ax,
                linewidth=self.lw / 4,
                solid_capstyle="round",
                # solid_joinstyle="miter",
                color=self.white,
            )
        ]

    def label(self, x, y, r, font_size, label):
        # draw station name
        loc = label.loc  # one of l, r, u, d, ul, ur, dl, dr

        loc_new = Coord(x, y).move(loc, length=r * 2)

        loc = "".join(sorted(loc))  # normalize

        ha, va = {
            "l": ("right", "center"),
            "r": ("left", "center"),
            "u": ("center", "bottom"),
            "d": ("center", "top"),
            "lu": ("right", "bottom"),
            "ru": ("left", "bottom"),
            "dl": ("right", "top"),
            "dr": ("left", "top"),
        }[loc]

        self.ax.text(
            loc_new.x,
            loc_new.y,
            label.name.upper(),
            ha=ha,
            va=va,
            rotation=label.ang,
            fontsize=font_size * self.font_size,
        )

    def railmap(self, railmap):
        for line in railmap.lines:
            self.line(line)
        for station in set(railmap.stations):
            self.station(station)
        for coord, station in railmap.interlining_stations:
            self.interlining(coord, station)
        xlow, xhigh, ylow, yhigh = railmap.bounds(self.coord_config, 1)

        self.fig.set_size_inches(xhigh - xlow, yhigh - ylow)
        self.ax.set_xlim(xlow, xhigh)
        self.ax.set_ylim(ylow, yhigh)
        self.ax.axis("equal")
        self.ax.axis("off")

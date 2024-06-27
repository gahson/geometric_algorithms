import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

class LineDrawer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.lines = []
        self.line = None
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.on_press)

    def on_press(self, event):
        if event.inaxes != self.ax:
            return

        if not self.line:
            self.line = [(event.xdata, event.ydata)]
        else:
            self.line.append((event.xdata, event.ydata))
            line = Line2D(*zip(*self.line), marker='o', color='b')
            self.ax.add_line(line)
            self.lines.append(tuple(self.line))
            self.line = []

        self.fig.canvas.draw()

    def get_lines(self):
        return self.lines

    def show_plot(self):
        plt.show()

if __name__ == '__main__':
    drawer = LineDrawer()
    print("Rysuj odcinki za pomocą myszki. Zakończ program, zamykając okno wykresu.")
    drawer.show_plot()

    lines = drawer.get_lines()
    print("Wprowadzone odcinki:")
    n=len(lines)
    for i in range(n):
        if i==0:
            print('[', end="")
        print(lines[i], end="")
        if i==n-1:
            print(']', end="")
        else:
            print(',')

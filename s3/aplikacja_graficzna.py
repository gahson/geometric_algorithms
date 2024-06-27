import tkinter as tk

class PolygonDrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Polygon Drawing App")

        self.canvas = tk.Canvas(self.root, width=500, height=500, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.points = []
        self.current_polygon = None

        self.canvas.bind("<Button-1>", self.on_click)

        self.finish_button = tk.Button(root, text="Zakończ", command=self.finish_drawing)
        self.finish_button.pack()

    def on_click(self, event):
        x, y = event.x, event.y
        self.points.append([x, y])

        if self.current_polygon:
            self.canvas.delete(self.current_polygon)

        self.current_polygon = self.canvas.create_polygon(self.points, outline="black", fill="", width=2)

    def finish_drawing(self):
        # Zamknij okno po zakończeniu rysowania
        self.root.destroy()

def draw_polygon():
    root = tk.Tk()
    app = PolygonDrawingApp(root)
    root.mainloop()

    # Po zamknięciu okna zwróć listę punktów wielokąta
    return app.points

if __name__ == "__main__":
    points = draw_polygon()
    for i in range( len(points)):
        points[i][1]*=(-1)
    print(points)



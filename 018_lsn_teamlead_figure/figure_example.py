from figure_class import Rectangle, Circle, Triangle

def main():
    specs = [
        ("Rectangle", (5, 5)),
        ("Rectangle", (10, 3)),
        ("Circle",    (3,)),
        ("Circle",    (7.5,)),
        ("Triangle",  (3, 4, 5)),
        ("Triangle",  (2, 2, 5)),
    ]

    for name, params in specs:
        try:
            if name == "Rectangle":
                fig = Rectangle(*params)
            elif name == "Circle":
                fig = Circle(*params)
            elif name == "Triangle":
                fig = Triangle(*params)
            else:
                continue

            print(fig)
            print(f"  Area:      {fig.area():.2f}")
            print(f"  Perimeter: {fig.perimeter():.2f}")
        except ValueError as e:
            print(f"[Error] {name}{params}: {e}")
        print("-" * 40)

if __name__ == "__main__":
    main()

from figure_class import Rectangle, Circle, Triangle


def main():
    figures = [
        Rectangle(5, 10),
        Circle(3),
        Triangle(3, 4, 5)
    ]

    for fig in figures:
        print(fig)
        print(f"  Area:      {fig.area():.2f}")
        print(f"  Perimeter: {fig.perimeter():.2f}")
        print("-" * 40)


if __name__ == "__main__":
    main()

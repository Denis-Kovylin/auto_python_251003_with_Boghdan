
class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __str__(self):
        return (
            f"Сторона А: {self.side_a}\n"
            f"Кут A: {self.angle_a}°\n"
            f"Кут B: {self.angle_b}°"
        )

    def __setattr__(self, key, value):
        if key == "side_a":
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError("side_a повинно бути числом більше за 0")

        elif key == "angle_a":
            if not isinstance(value, (int, float)) or not (1 <= value <= 179):
                raise ValueError("angle_a повинно бути в межах від 1 до 179")

            super().__setattr__("angle_b", 180 - value)
            
        super().__setattr__(key, value)


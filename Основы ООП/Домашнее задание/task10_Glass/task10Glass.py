from typing import Union


class Glass:
    def __init__(self, material: Union[str]):
        self.material = self.get_material(material)

    def get_material(self, material):
        material = input()
        return self.material

    def __str__(self):
        return f"Материал, из которого сделан стакан: {self.material}"


if __name__ == "__main__":
    glass = Glass()

    print(glass)

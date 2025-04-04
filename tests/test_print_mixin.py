from src.classes import Product, Smartphone, LawnGrass

def test_print_mixin_smartphone(capsys):
    Smartphone("Смартфон", "Последний ипхон", 90_000, 395,
               "очень хорошая", "16 Pro", "256", "Blue")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Смартфон, Последний ипхон, 90000, 395)"


def test_print_mixin_lawngrass(capsys):
    LawnGrass("Трава для газона", "красивая", 10_000, 314,
              "China", "10 days", "ярко-зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Трава для газона, красивая, 10000, 314)"


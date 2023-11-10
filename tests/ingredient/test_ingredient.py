from src.models.ingredient import (
    Ingredient,
    Restriction,
    )


def test_ingredient():
    ingredient_one = Ingredient("manteiga")
    ingredient_two = Ingredient("manteiga")
    ingredient_three = Ingredient("queijo_mussarela")

    assert hash(ingredient_one) == hash(ingredient_two)
    assert hash(ingredient_one) != hash(ingredient_three)
    assert ingredient_one.__eq__(ingredient_two) is True
    assert ingredient_one.__eq__(ingredient_three) is False
    assert ingredient_one == ingredient_two
    assert ingredient_one.name == "manteiga"
    assert repr(ingredient_three) == "Ingredient('queijo mussarela')"
    assert ingredient_three.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

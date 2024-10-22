from src.models.ingredient import (
    Ingredient,
    Restriction,
)


def test_ingredient():
    ingredient_one = Ingredient("manteiga")
    ingredient_two = Ingredient("manteiga")
    ingredient_three = Ingredient("camarão")

    assert ingredient_one == ingredient_two
    assert ingredient_one != ingredient_three

    assert hash(ingredient_one) == hash(ingredient_two)
    assert hash(ingredient_one) != hash(ingredient_three)
    assert ingredient_three.name == "camarão"

    assert ingredient_one.__eq__(ingredient_two) is True
    assert ingredient_one.__eq__(ingredient_three) is False

    assert repr(ingredient_three) == "Ingredient('camarão')"

    assert ingredient_three.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }

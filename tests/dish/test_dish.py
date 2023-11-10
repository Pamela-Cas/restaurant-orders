from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501

import pytest


# Req 2
def test_dish():
    test_one = Dish("camarão", 25.90)
    test_two = Dish("lasanha berinjela", 27.0)
    assert test_one.name == "camarão"
    assert test_one == test_one
    assert test_two.price == 27.0
    assert hash(test_two) == hash(test_two)
    assert hash(test_two) != hash(test_one)
    assert repr(test_one) == "Dish('camarão', R$25.90)"
    verify_ingredient = Ingredient("camarão")
    test_one.add_ingredient_dependency(verify_ingredient, 10)
    assert test_one.get_ingredients() == {Ingredient("camarão")}
    restrictions = test_one.get_restrictions()
    assert restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
    with pytest.raises(TypeError):
        Dish("sobremesa", "11.17")
    with pytest.raises(ValueError):
        Dish("sobremesa", 0)

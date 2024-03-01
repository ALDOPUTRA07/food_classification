from food_classification.processing.data_manager import (
    class_name,
    data_loader,
    load_data,
)


def test_load_data():
    # act
    train_data, test_data = load_data()

    # assert
    assert train_data.classes == ["pizza", "steak", "sushi"]
    assert len(test_data) == 75


def test_class_name(load_dataset):
    # arrange
    train_data = load_dataset

    # act
    classes_name = class_name(train_data)

    # assert
    assert classes_name == ["pizza", "steak", "sushi"]


def test_data_loader(load_dataset):
    # act
    train_dataloader, _ = data_loader(1, 1)
    img, label = next(iter(train_dataloader))

    # assert
    assert label.shape[0] == 1

import pytest
from src.make_features import img_to_vector, load_header_df, header_to_img_matrix

def test_image_file_to_vector():

    
    # Can open and convert a normal preprocessed image
    fn = '0_right.jpg'
    img = img_to_vector(fn)
    assert img.shape == (1, 512*512*3)

    # Can resize an image
    img = img_to_vector(fn, resize=(150,150))
    assert img.shape == (1, 150*150*3)

    # Will raise type error for a bad resize value
    with pytest.raises(TypeError):
        img_to_vector(fn, resize='a')

    # Will raise value error for wrong directory
    with pytest.raises(ValueError):
        img_to_vector(fn, resize='a', imgdir='data/hello')

def test_load_header_df():
    df = load_header_df()

    # CSV should have data in it
    assert df.shape[0] > 0

    # Data should contain the necessary columns
    assert 'filename' in df.columns.values

def test_header_to_image_matrix():

    df = load_header_df().sample(10)

    header, images = header_to_img_matrix(df)

    # header array should have same shape as df
    assert df.shape == header.shape
    # header and images should have same number of rows
    assert images.shape[0] == df.shape[0]
    # image columns should be default 512x512 with 3 color channels
    assert images.shape[1] == 512*512*3

    _, images_resized = header_to_img_matrix(df, (50,50))
    # image resize should work
    assert images_resized.shape[1] == 50*50*3


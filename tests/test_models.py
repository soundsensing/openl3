import openl3.core
from openl3.models import (
    load_audio_embedding_model, get_audio_embedding_model_path,
    load_image_embedding_model, get_image_embedding_model_path)
from openl3.openl3_exceptions import OpenL3Error
import pytest


INPUT_REPR_SIZES = {
    'linear': (None, 257, 197, 1),
    'mel128': (None, 128, 199, 1),
    'mel256': (None, 256, 199, 1),
}
CONTENT_TYPES = ['env', 'music']

@pytest.mark.parametrize('input_repr', list(INPUT_REPR_SIZES))
@pytest.mark.parametrize('content_type', CONTENT_TYPES)
def test_get_audio_embedding_model_path(input_repr, content_type):
    embedding_model_path = get_audio_embedding_model_path(input_repr, content_type)
    assert (
        '/'.join(embedding_model_path.split('/')[-2:]) == 
        'openl3/openl3_audio_{}_{}.h5'.format(input_repr, content_type))


def test_load_audio_embedding_model():
    import kapre

    m = load_audio_embedding_model('linear', 'music', 6144)
    # assert isinstance(m.layers[1], kapre.time_frequency.Spectrogram)
    assert m.layers[1].output_shape == (None, 257, 197, 1)
    assert m.output_shape[1] == 6144

    first_model = m

    m = load_audio_embedding_model('linear', 'music', 512)
    # assert isinstance(m.layers[1], kapre.time_frequency.Spectrogram)
    assert m.layers[1].output_shape == (None, 257, 197, 1)
    assert m.output_shape[1] == 512
    # Check model consistency
    assert isinstance(m.layers[0], type(first_model.layers[0]))
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers[2:], first_model.layers[2:])])

    m = load_audio_embedding_model('linear', 'env', 6144)
    # assert isinstance(m.layers[1], kapre.time_frequency.Spectrogram)
    assert m.layers[1].output_shape == (None, 257, 197, 1)
    assert m.output_shape[1] == 6144
    # Check model consistency
    assert isinstance(m.layers[0], type(first_model.layers[0]))
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers[2:], first_model.layers[2:])])

    m = load_audio_embedding_model('linear', 'env', 512)
    # assert isinstance(m.layers[1], kapre.time_frequency.Spectrogram)
    assert m.layers[1].output_shape == (None, 257, 197, 1)
    assert m.output_shape[1] == 512
    # Check model consistency
    assert isinstance(m.layers[0], type(first_model.layers[0]))
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers[2:], first_model.layers[2:])])

    m = load_audio_embedding_model('mel128', 'music', 6144)
    # assert isinstance(m.layers[1], kapre.time_frequency.Melspectrogram)
    assert m.layers[1].output_shape == (None, 128, 199, 1)
    assert m.output_shape[1] == 6144
    # Check model consistency
    assert isinstance(m.layers[0], type(first_model.layers[0]))
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers[2:], first_model.layers[2:])])

    m = load_audio_embedding_model('mel128', 'music', 512)
    # assert isinstance(m.layers[1], kapre.time_frequency.Melspectrogram)
    assert m.layers[1].output_shape == (None, 128, 199, 1)
    assert m.output_shape[1] == 512
    # Check model consistency
    assert isinstance(m.layers[0], type(first_model.layers[0]))
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers[2:], first_model.layers[2:])])

    m = load_audio_embedding_model('mel128', 'env', 6144)
    # assert isinstance(m.layers[1], kapre.time_frequency.Melspectrogram)
    assert m.layers[1].output_shape == (None, 128, 199, 1)
    assert m.output_shape[1] == 6144
    # Check model consistency
    assert isinstance(m.layers[0], type(first_model.layers[0]))
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers[2:], first_model.layers[2:])])

    m = load_audio_embedding_model('mel128', 'env', 512)
    # assert isinstance(m.layers[1], kapre.time_frequency.Melspectrogram)
    assert m.layers[1].output_shape == (None, 128, 199, 1)
    assert m.output_shape[1] == 512
    # Check model consistency
    assert isinstance(m.layers[0], type(first_model.layers[0]))
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers[2:], first_model.layers[2:])])

    m = load_audio_embedding_model('mel256', 'music', 6144)
    # assert isinstance(m.layers[1], kapre.time_frequency.Melspectrogram)
    assert m.layers[1].output_shape == (None, 256, 199, 1)
    assert m.output_shape[1] == 6144
    # Check model consistency
    assert isinstance(m.layers[0], type(first_model.layers[0]))
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers[2:], first_model.layers[2:])])

    m = load_audio_embedding_model('mel256', 'music', 512)
    # assert isinstance(m.layers[1], kapre.time_frequency.Melspectrogram)
    assert m.layers[1].output_shape == (None, 256, 199, 1)
    assert m.output_shape[1] == 512
    # Check model consistency
    assert isinstance(m.layers[0], type(first_model.layers[0]))
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers[2:], first_model.layers[2:])])

    m = load_audio_embedding_model('mel256', 'env', 6144)
    # assert isinstance(m.layers[1], kapre.time_frequency.Melspectrogram)
    assert m.layers[1].output_shape == (None, 256, 199, 1)
    assert m.output_shape[1] == 6144
    # Check model consistency
    assert isinstance(m.layers[0], type(first_model.layers[0]))
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers[2:], first_model.layers[2:])])

    m = load_audio_embedding_model('mel256', 'env', 512)
    # assert isinstance(m.layers[1], kapre.time_frequency.Melspectrogram)
    assert m.layers[1].output_shape == (None, 256, 199, 1)
    assert m.output_shape[1] == 512
    # Check model consistency
    assert isinstance(m.layers[0], type(first_model.layers[0]))
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers[2:], first_model.layers[2:])])


def _compare_layers(layersA, layersB):
    assert len(layersA) == len(layersB)
    for la, lb in zip(layersA, layersB):
        assert type(la) == type(lb)
        assert la.input_shape == lb.input_shape
        assert la.output_shape == lb.output_shape


@pytest.mark.parametrize('input_repr', list(INPUT_REPR_SIZES))
def test_frontend(input_repr):
    # check spectrogram input size
    m = load_audio_embedding_model(input_repr, 'env', 512, frontend='librosa')
    assert m.input_shape == INPUT_REPR_SIZES[input_repr]

    m2 = load_audio_embedding_model(input_repr, 'env', 512, frontend='kapre')
    assert m2.input_shape == (None, 1, openl3.core.TARGET_SR)

    # compare all layers to model with frontend
    _compare_layers(m.layers[1:], m2.layers[2:])

    with pytest.raises(OpenL3Error):
        load_audio_embedding_model(input_repr, 'env', 512, frontend='not-a-thing')


def test_validate_audio_frontend():
    input_repr = 'mel128'

    # test kapre
    mk = load_audio_embedding_model(input_repr, 'env', 512, frontend='kapre')
    assert len(mk.input_shape) == 3
    # assert openl3.models._validate_audio_frontend('infer', input_repr, mk) == ('kapre', input_repr)
    assert openl3.models._validate_audio_frontend('kapre', input_repr, mk) == ('kapre', input_repr)

    # test librosa validate
    ml = load_audio_embedding_model(input_repr, 'env', 512, frontend='librosa')
    assert len(ml.input_shape) == 4
    # assert openl3.models._validate_audio_frontend('infer', input_repr, ml) == ('librosa', input_repr)
    assert openl3.models._validate_audio_frontend('librosa', input_repr, ml) == ('librosa', input_repr)

    # test frontend + no input_repr
    assert openl3.models._validate_audio_frontend('kapre', None, mk) == ('kapre', 'mel256')
    with pytest.raises(OpenL3Error):
        openl3.models._validate_audio_frontend('librosa', None, ml)
    
    # test mismatched frontend/model
    with pytest.raises(OpenL3Error):
        openl3.models._validate_audio_frontend('librosa', None, mk)
    with pytest.raises(OpenL3Error):
        openl3.models._validate_audio_frontend('kapre', None, ml)


@pytest.mark.parametrize('input_repr', list(INPUT_REPR_SIZES))
@pytest.mark.parametrize('content_type', CONTENT_TYPES)
def test_get_image_embedding_model_path(input_repr, content_type):
    embedding_model_path = get_image_embedding_model_path(input_repr, content_type)
    assert (
        '/'.join(embedding_model_path.split('/')[-2:]) == 
        'openl3/openl3_image_{}_{}.h5'.format(input_repr, content_type))


def test_load_image_embedding_model():
    m = load_image_embedding_model('linear', 'music', 8192)
    assert m.output_shape[1] == 8192

    first_model = m

    m = load_image_embedding_model('linear', 'music', 512)
    assert m.output_shape[1] == 512
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers, first_model.layers)])

    m = load_image_embedding_model('linear', 'env', 8192)
    assert m.output_shape[1] == 8192
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers, first_model.layers)])

    m = load_image_embedding_model('linear', 'env', 512)
    assert m.output_shape[1] == 512
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers, first_model.layers)])

    m = load_image_embedding_model('mel128', 'music', 8192)
    assert m.output_shape[1] == 8192
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers, first_model.layers)])

    m = load_image_embedding_model('mel128', 'music', 512)
    assert m.output_shape[1] == 512
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers, first_model.layers)])

    m = load_image_embedding_model('mel128', 'env', 8192)
    assert m.output_shape[1] == 8192
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers, first_model.layers)])

    m = load_image_embedding_model('mel128', 'env', 512)
    assert m.output_shape[1] == 512
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers, first_model.layers)])

    m = load_image_embedding_model('mel256', 'music', 8192)
    assert m.output_shape[1] == 8192
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers, first_model.layers)])

    m = load_image_embedding_model('mel256', 'music', 512)
    assert m.output_shape[1] == 512
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers, first_model.layers)])

    m = load_image_embedding_model('mel256', 'env', 8192)
    assert m.output_shape[1] == 8192
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers, first_model.layers)])

    m = load_image_embedding_model('mel256', 'env', 512)
    assert m.output_shape[1] == 512
    assert len(m.layers) == len(first_model.layers)
    assert all([isinstance(l1, type(l2))
                for (l1, l2) in zip(m.layers, first_model.layers)])

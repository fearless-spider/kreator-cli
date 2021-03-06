
from pytest import raises
from kreator.main import KreatorTest

def test_kreator():
    # test kreator without any subcommands or arguments
    with KreatorTest() as app:
        app.run()
        assert app.exit_code == 0


def test_kreator_debug():
    # test that debug mode is functional
    argv = ['--debug']
    with KreatorTest(argv=argv) as app:
        app.run()
        assert app.debug is True


def test_command1():
    # test command1 without arguments
    argv = ['command1']
    with KreatorTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'bar'
        assert output.find('Foo => bar')


    # test command1 with arguments
    argv = ['command1', '--foo', 'not-bar']
    with KreatorTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'not-bar'
        assert output.find('Foo => not-bar')


def test_pyramid():
    # test command1 without arguments
    argv = ['pyramid']
    with KreatorTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        output.find('Pyramid')

    # test command1 with arguments
    argv = ['pyramid', '--config', 'kreator.yml']
    with KreatorTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['config'] == 'kreator.yml'

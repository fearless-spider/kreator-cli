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


def test_pyramid():
    # test pyramid without arguments
    argv = ['pyramid']
    with KreatorTest(argv=argv) as app:
        app.run()
        data, output = app.last_rendered
        output.find('Pyramid')

    # test pyramid with arguments
    argv = ['pyramid', '--config', 'kreator.yml']
    with KreatorTest(argv=argv) as app:
        app.run()
        data, output = app.last_rendered
        assert data['config'] == 'kreator.yml'


def test_django():
    argv = ['django']
    with KreatorTest(argv=argv) as app:
        app.run()
        data, output = app.last_rendered
        output.find('Django')

    argv = ['django', '--config', 'kreator.yml']
    with KreatorTest(argv=argv) as app:
        app.run()
        data, output = app.last_rendered
        assert data['config'] == 'kreator.yml'

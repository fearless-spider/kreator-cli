from cement import Controller, ex


class Pyramid(Controller):

    class Meta:
        label = 'Pyramid'
        stacked_on = 'base'
        stacked_type = 'embedded'
        # text displayed at the top of --help output
        description = 'This component generate pyramid app'

        # text displayed at the bottom of --help output
        epilog = 'Usage: kreator pyramid --config kreator.yml'

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()

    @ex(
        help='kreator pyramid -c kreator.yml',
        # sub-command level arguments. ex: 'kreator command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            (['-c', '--config'],
             {'help': 'Config file to new pyramid app',
              'action': 'store',
              'dest': 'config'})
        ],
    )
    def pyramid(self):
        """Pyramid sub-command."""

        data = {
        }

        if self.app.pargs.config is not None:
            data['config'] = self.app.pargs.config

        self.app.render(data, 'pyramid.jinja2')

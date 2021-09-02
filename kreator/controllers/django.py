from cement import Controller, ex


class Django(Controller):

    class Meta:
        label = 'Django'
        stacked_on = 'base'
        stacked_type = 'embedded'
        # text displayed at the top of --help output
        description = 'This component generate django app, models and more'

        # text displayed at the bottom of --help output
        epilog = 'Usage: kreator django --config kreator.yml'

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()

    @ex(
        help='kreator django -c kreator.yml',
        # sub-command level arguments. ex: 'kreator command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            (['-c', '--config'],
             {'help': 'Config file to new django app, models,...',
              'action': 'store',
              'dest': 'config'})
        ],
    )
    def django(self):
        """Django sub-command."""

        data = {
        }

        if self.app.pargs.config is not None:
            data['config'] = self.app.pargs.config

        self.app.render(data, 'django.jinja2')

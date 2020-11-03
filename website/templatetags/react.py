from django import template


register = template.Library()


QUOTES = '"', "'"


@register.simple_tag(takes_context=True)
def react_import(context, module):
    output = context.template.engine.get_template('react-import.pug')
    return output.render(template.Context({'module': module}))


@register.tag
def react(parser, token):
    tag_name, *contents = token.split_contents()
    if len(contents) != 2:
        raise template.TemplateSyntaxError('react takes 2 arguments')
    widget = parse_argument(contents[0])
    selector = parse_argument(contents[1])
    nodelist = parser.parse(('endreact',))
    parser.delete_first_token()
    return ReactNode(widget, selector, nodelist)


class ReactNode(template.Node):
    
    def __init__(self, widget, selector, nodelist):
        self.widget = widget
        self.selector = selector
        self.nodelist = nodelist

    def render(self, context):
        output = context.template.engine.get_template('react-widget.pug')
        props = self.nodelist.render(context)
        props = props.replace('<script', '<script type="text/babel"', 1)
        return output.render(template.Context({
            'widget': self.widget(context),
            'selector': self.selector(context),
            'props': props,
        }, autoescape=context.autoescape))


def parse_argument(string):
    if string.startswith(QUOTES):
        return lambda context: string[1:-1]
    else:
        return lambda context: template.Variable(string).resolve(context)

from jinja2.ext import InternationalizationExtension, Extension
from jinja2.exceptions import TemplateSyntaxError
from jinja2 import lexer
from jinja2 import nodes
from jdj_tags.extensions import DjangoI18n
import django.dispatch

class DjangoInternationalizationExtension(DjangoI18n,
                                          InternationalizationExtension):
    tags = {'trans', 'blocktrans'}

    def __init__(self, environment):
        DjangoI18n.__init__(self, environment)
        InternationalizationExtension.__init__(self, environment)

    def parse(self, parser):
        token = next(parser.stream)
        if token.value == 'blocktrans':
            return self._parse_blocktrans(parser, token.lineno)
        else:
            if parser.stream.current.type == 'string':
                return self._parse_trans(parser, token.lineno)
            else:
                parser.stream.push(parser.stream.current)
                parser.stream.current = token
                return InternationalizationExtension.parse(self, parser)


class DjangoComment(Extension):
    """Support django's comment tag.

    Jinja has a better comment system. However this eases converting Django
    templates to Jinja."""

    tags = {'comment'}

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        body = parser.parse_statements(['name:endcomment'], drop_needle=True)
        return []


class DjangoLoad(Extension):
    """A dummy django's load tag."""

    tags = {'load'}

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        args = parser.parse_expression()
        return []

menu_done = django.dispatch.Signal(providing_args=["menu"]) 

class CodeschoolSubject(Extension):
	tags = {'pldispatch'}

	def parse(self,parser):
		lineno = next(parser.stream).lineno

        # now we parse a single expression that is used as cache key.
		args = [parser.parse_expression()]
		body = parser.parse_statements(['name:endpldispatch'], drop_needle=True)
		print(lineno,args,body)
		return nodes.CallBlock(self.call_method("_tratar_dispatch",args),
								[],[],body).set_lineno(lineno)	

	def _tratar_dispatch(self,name, caller):
		menu = ["Teste"]
		menu_done.send(sender=self.__class__, menu = menu)	
		total = ""
		for m in menu:
			total += m
		return total
#
# This is a hacky and ugly solution. Probably we should send a patch to djinga.
# Ugly as it is, it works ;-)
#
import jinja2.ext
jinja2.ext.i18n = i18n = DjangoInternationalizationExtension


from parglare import Grammar, Parser

from ir import ir_actions


class SysqlMongoCompiler(object):
    def __init__(self):
        self.grammar = self.build_grammar('sysql.pg')
        self.parser = self.build_parser(self.grammar, ir_actions)

    def build_grammar(self, grammar_file_path):
        grammar = Grammar.from_file(grammar_file_path)
        return grammar

    def build_parser(self, grammar, actions):
        parser = Parser(grammar, actions=actions)
        return parser

    def parse(self, query):
        return self.parser.parse(query)

    def remove_not(self, ir_representation):
        return ir_representation.remove_not()

    def optimize(self, without_not_ir):
        return without_not_ir.optimize()

    def str_mongo(self, optimized_ir):
        return optimized_ir.str_mongo()

    def prepare_header(self, header):
        if header is None:
            return ""
        return header.str_mongo()

    def compile(self, query):
        print("Sysql query      : %s" % query)
        ir_representation_and_header = self.parse(query)
        ir_representation = ir_representation_and_header.query
        header = ir_representation_and_header.header
        print("IR reprezentation: %s" % ir_representation)
        without_not_ir = self.remove_not(ir_representation)
        print("Not removed      : %s" % without_not_ir)
        optimized_ir = self.optimize(without_not_ir)
        print("Optimized IR     : %s" % optimized_ir)
        str_mongo_query = self.str_mongo(optimized_ir)
        str_header = self.prepare_header(header)
        print("Mongo query      : %s" % str_mongo_query)
        full_query = str_mongo_query + ";" + str_header if str_header else str_mongo_query
        print("Response: %s" % full_query)
        return full_query


sysqo = SysqlMongoCompiler()
# query = "not (last(1Y 2M 3D 1h 2m 3s)) or last(1Y)"
# query = "before(2014-11-12) and not severity<10; page(3), limit(5), sort(hostname:asc, appname:desc)"

# query = "last(1s) and appname=/.*Fa.*/; limit(5), page(0)"
# query = "msg=/$from.*/"
# query = r'appname="asda\"sd\"asd" and hostname="cao \" kako si" and appname=/\/\/asdasd\//
# and hostname=/ovo ide\/ovo ne ide/'

query = r'not(severity!=1 or facility!=2) and hostname="machine1" and appname="app3"'
mongo_query = sysqo.compile(query)


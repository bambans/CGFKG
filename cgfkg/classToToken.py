import ast

astToTokenList = {
    ast.AST: {
        'tokenValue': ''
    },
    ast.mod: {
        'tokenValue': ''
    },
    ast.Module: {
        'tokenValue': '',
        'body':{
            'open': '',
            'close': ''
        },
        'type_ignores':{
            'open': '',
            'close': ''
        }
    },
    ast.Interactive: {
        'tokenValue': '',
        'body':{
            'open': '',
            'close': ''
        }
    },
    ast.Expression: {
        'tokenValue': '',
        'body':{
            'open': '',
            'close': ''
        }
    },
    ast.FunctionType: {
        'tokenValue': '',
        'argtypes':{
            'open': '',
            'close': ''
        },
        'returns':{
            'open': '',
            'close': ''
        }
    },
    ast.Suite: {
        'tokenValue': ''
    },
    ast.stmt: {
        'tokenValue': ''
    },
    ast.FunctionDef: {
        'tokenValue': 'def ',
        'name':{
            'open': '',
            'close': ''
        },
        'args':{
            'open': '(',
            'close': '):\n'
        },
        'body':{
            'open': '\t',
            'close': '\n'
        },
        'decorator_list':{
            'open': '',
            'close': ''
        },
        'returns':{
            'open': '',
            'close': ''
        },
        'type_comment':{
            'open': '',
            'close': ''
        }
    },
    ast.AsyncFunctionDef: {
        'tokenValue': '',
        'name':{
            'open': '',
            'close': ''
        },
        'args':{
            'open': '',
            'close': ''
        },
        'body':{
            'open': '',
            'close': ''
        },
        'decorator_list':{
            'open': '',
            'close': ''
        },
        'returns':{
            'open': '',
            'close': ''
        },
        'type_comment':{
            'open': '',
            'close': ''
        }
    },
    ast.ClassDef: {
        'tokenValue': 'class ',
        'name':{
            'open': '',
            'close': ''
        },
        'bases':{
            'open': '',
            'close': ''
        },
        'keywords':{
            'open': '',
            'close': ''
        },
        'body':{
            'open': '',
            'close': ''
        },
        'decorator_list':{
            'open': '',
            'close': ''
        }
    },
    ast.Return: {
        'tokenValue': 'return ',
        'value':{
            'open': '',
            'close': '\n'
        }
    },
    ast.Delete: {
        'tokenValue': '',
        'targets':{
            'open': '',
            'close': ''
        }
    },
    ast.Assign: {
        'tokenValue': '',
        'targets':{
            'open': '',
            'close': ''
        },
        'value':{
            'open': ' = ',
            'close': ''
        },
        'type_comment':{
            'open': '',
            'close': ''
        }
    },
    ast.AugAssign: {
        'tokenValue': '',
        'target':{
            'open': '',
            'close': ''
        },
        'op':{
            'open': '',
            'close': ''
        },
        'value':{
            'open': '',
            'close': ''
        }
    },
    ast.AnnAssign: {
        'tokenValue': '',
        'target':{
            'open': '',
            'close': ''
        },
        'annotation':{
            'open': '',
            'close': ''
        },
        'value':{
            'open': '',
            'close': ''
        },
        'simple':{
            'open': '',
            'close': ''
        }
    },
    ast.For: {
        'tokenValue': 'for ',
        'target':{
            'open': '',
            'close': ''
        },
        'iter':{
            'open': '',
            'close': ''
        },
        'body':{
            'open': '',
            'close': ''
        },
        'orelse':{
            'open': '',
            'close': ''
        },
        'type_comment':{
            'open': '',
            'close': ''
        }
    },
    ast.AsyncFor: {
        'tokenValue': '',
        'target':{
            'open': '',
            'close': ''
        },
        'iter':{
            'open': '',
            'close': ''
        },
        'body':{
            'open': '',
            'close': ''
        },
        'orelse':{
            'open': '',
            'close': ''
        },
        'type_comment':{
            'open': '',
            'close': ''
        }
    },
    ast.While: {
        'tokenValue': 'while ',
        'test':{
            'open': '',
            'close': ':\n'
        },
        'body':{
            'open': '',
            'close': '\n'
        },
        'orelse':{
            'open': '',
            'close': ''
        }
    },
    ast.If: {
        'tokenValue': 'if ',
        'test':{
            'open': '',
            'close': ':\n'
        },
        'body':{
            'open': '\t',
            'close': '\n'
        },
        'orelse':{
            'open': '',
            'close': ''
        }
    },
    ast.With: {
        'tokenValue': 'with ',
        'items':{
            'open': '',
            'close': ':'
        },
        'body':{
            'open': '',
            'close': ''
        },
        'type_comment':{
            'open': '',
            'close': ''
        }
    },
    ast.AsyncWith: {
        'tokenValue': '',
        'items':{
            'open': '',
            'close': ''
        },
        'body':{
            'open': '',
            'close': ''
        },
        'type_comment':{
            'open': '',
            'close': ''
        }
    },
    ast.Match: {
        'tokenValue': '',
        'subject':{
            'open': '',
            'close': ''
        },
        'cases':{
            'open': '',
            'close': ''
        }
    },
    ast.Raise: {
        'tokenValue': '',
        'exc':{
            'open': '',
            'close': ''
        },
        'cause':{
            'open': '',
            'close': ''
        }
    },
    ast.Try: {
        'tokenValue': 'try:\n',
        'body':{
            'open': '',
            'close': ''
        },
        'handlers':{
            'open': '',
            'close': ''
        },
        'orelse':{
            'open': '',
            'close': ''
        },
        'finalbody':{
            'open': '',
            'close': ''
        }
    },
    ast.TryStar: {
        'tokenValue': '',
        'body':{
            'open': '',
            'close': ''
        },
        'handlers':{
            'open': '',
            'close': ''
        },
        'orelse':{
            'open': '',
            'close': ''
        },
        'finalbody':{
            'open': '',
            'close': ''
        }
    },
    ast.Assert: {
        'tokenValue': '',
        'test':{
            'open': '',
            'close': ''
        },
        'msg':{
            'open': '',
            'close': ''
        }
    },
    ast.Import: {
        'tokenValue': 'import ',
        'names':{
            'open': '',
            'close': ''
        }
    },
    ast.ImportFrom: {
        'tokenValue': 'from ',
        'module':{
            'open': '',
            'close': ' import '
        },
        'names':{
            'open': '',
            'close': '\n'
        },
        'level':{
            'open': '',
            'close': ''
        }
    },
    ast.Global: {
        'tokenValue': 'global ',
        'names':{
            'open': '',
            'close': ''
        }
    },
    ast.Nonlocal: {
        'tokenValue': '',
        'names':{
            'open': '',
            'close': ''
        }
    },
    ast.Expr: {
        'tokenValue': '',
        'value':{
            'open': '',
            'close': ''
        }
    },
    ast.Pass: {
        'tokenValue': 'pass '
    },
    ast.Break: {
        'tokenValue': 'break '
    },
    ast.Continue: {
        'tokenValue': 'continue '
    },
    ast.expr: {
        'tokenValue': ''
    },
    ast.BoolOp: {
        'tokenValue': '',
        'op':{
            'open': '',
            'close': ''
        },
        'values':{
            'open': '',
            'close': ''
        }
    },
    ast.NamedExpr: {
        'tokenValue': '',
        'target':{
            'open': '',
            'close': ''
        },
        'value':{
            'open': '',
            'close': ''
        }
    },
    ast.BinOp: {
        'tokenValue': '',
        'left':{
            'open': '',
            'close': ''
        },
        'op':{
            'open': '',
            'close': ''
        },
        'right':{
            'open': '',
            'close': ''
        }
    },
    ast.UnaryOp: {
        'tokenValue': '',
        'op':{
            'open': '',
            'close': ''
        },
        'operand':{
            'open': '',
            'close': ''
        }
    },
    ast.Lambda: {
        'tokenValue': 'lambda ',
        'args':{
            'open': '',
            'close': ''
        },
        'body':{
            'open': '',
            'close': ''
        }
    },
    ast.IfExp: {
        'tokenValue': '',
        'test':{
            'open': '',
            'close': ''
        },
        'body':{
            'open': '',
            'close': ''
        },
        'orelse':{
            'open': '',
            'close': ''
        }
    },
    ast.Dict: {
        'tokenValue': '',
        'keys':{
            'open': '',
            'close': ''
        },
        'values':{
            'open': '',
            'close': ''
        }
    },
    ast.Set: {
        'tokenValue': '',
        'elts':{
            'open': '',
            'close': ''
        }
    },
    ast.ListComp: {
        'tokenValue': '',
        'elt':{
            'open': '',
            'close': ''
        },
        'generators':{
            'open': '',
            'close': ''
        }
    },
    ast.SetComp: {
        'tokenValue': '',
        'elt':{
            'open': '',
            'close': ''
        },
        'generators':{
            'open': '',
            'close': ''
        }
    },
    ast.DictComp: {
        'tokenValue': '',
        'key':{
            'open': '',
            'close': ''
        },
        'value':{
            'open': '',
            'close': ''
        },
        'generators':{
            'open': '',
            'close': ''
        }
    },
    ast.GeneratorExp: {
        'tokenValue': '',
        'elt':{
            'open': '',
            'close': ''
        },
        'generators':{
            'open': '',
            'close': ''
        }
    },
    ast.Await: {
        'tokenValue': '',
        'value':{
            'open': '',
            'close': ''
        }
    },
    ast.Yield: {
        'tokenValue': 'yield ',
        'value':{
            'open': '',
            'close': ''
        }
    },
    ast.YieldFrom: {
        'tokenValue': 'yield from ',
        'value':{
            'open': '',
            'close': ''
        }
    },
    ast.Compare: {
        'tokenValue': '',
        'left':{
            'open': '',
            'close': ''
        },
        'ops':{
            'open': '',
            'close': ''
        },
        'comparators':{
            'open': '',
            'close': ''
        }
    },
    ast.Call: {
        'tokenValue': '',
        'func':{
            'open': '',
            'close': ''
        },
        'args':{
            'open': '(',
            'close': ')\n'
        },
        'keywords':{
            'open': '',
            'close': ''
        }
    },
    ast.FormattedValue: {
        'tokenValue': '',
        'value':{
            'open': '',
            'close': ''
        },
        'conversion':{
            'open': '',
            'close': ''
        },
        'format_spec':{
            'open': '',
            'close': ''
        }
    },
    ast.JoinedStr: {
        'tokenValue': '',
        'values':{
            'open': '',
            'close': ''
        }
    },
    ast.Constant: {
        'tokenValue': '',
        'value':{
            'open': '',
            'close': ''
        # }
        },
        'kind':{
            'open': '',
            'close': ''
        }
    },
    ast.Num: {
        'tokenValue': '',
        'n':{
            'open': '',
            'close': ''
        }
    },
    ast.Str: {
        'tokenValue': '',
        's':{
            'open': '',
            'close': ''
        }
    },
    ast.Bytes: {
        'tokenValue': '',
        's':{
            'open': '',
            'close': ''
        }
    },
    ast.NameConstant: {
        'tokenValue': '',
        'value':{
            'open': '',
            'close': ''
        },
        'kind':{
            'open': '',
            'close': ''
        }
    },
    ast.Ellipsis: {
        'tokenValue': '... '
    },
    ast.Attribute: {
        'tokenValue': '',
        'value':{
            'open': '',
            'close': '.'
        },
        'attr':{
            'open': '',
            'close': ''
        },
        'ctx':{
            'open': '',
            'close': ''
        }
    },
    ast.Subscript: {
        'tokenValue': '',
        'value':{
            'open': '',
            'close': ''
        },
        'slice':{
            'open': '',
            'close': ''
        },
        'ctx':{
            'open': '',
            'close': ''
        }
    },
    ast.Starred: {
        'tokenValue': '',
        'value':{
            'open': '',
            'close': ''
        },
        'ctx':{
            'open': '',
            'close': ''
        }
    },
    ast.Name: {
        'tokenValue': '',
        'id':{
            'open': '',
            'close': ''
        },
        'ctx':{
            'open': '',
            'close': ''
        }
    },
    ast.List: {
        'tokenValue': '',
        'elts':{
            'open': '',
            'close': ''
        },
        'ctx':{
            'open': '',
            'close': ''
        }
    },
    ast.Tuple: {
        'tokenValue': '',
        'elts':{
            'open': '',
            'close': ''
        },
        'ctx':{
            'open': '',
            'close': ''
        }
    },
    ast.Slice: {
        'tokenValue': '',
        'lower':{
            'open': '',
            'close': ''
        },
        'upper':{
            'open': '',
            'close': ''
        },
        'step':{
            'open': '',
            'close': ''
        }
    },
    ast.expr_context: {
        'tokenValue': ''
    },
    ast.Load: {
        'tokenValue': ' = '
    },
    ast.Store: {
        'tokenValue': ' = '
    },
    ast.Del: {
        'tokenValue': ''
    },
    ast.AugLoad: {
        'tokenValue': '= '
    },
    ast.AugStore: {
        'tokenValue': '= '
    },
    ast.Param: {
        'tokenValue': ''
    },
    ast.boolop: {
        'tokenValue': ''
    },
    ast.And: {
        'tokenValue': 'and '
    },
    ast.Or: {
        'tokenValue': 'or '
    },
    ast.operator: {
        'tokenValue': ''
    },
    ast.Add: {
        'tokenValue': '+ '
    },
    ast.Sub: {
        'tokenValue': '- '
    },
    ast.Mult: {
        'tokenValue': '* '
    },
    ast.MatMult: {
        'tokenValue': '@ '
    },
    ast.Div: {
        'tokenValue': '/ '
    },
    ast.Mod: {
        'tokenValue': '% '
    },
    ast.Pow: {
        'tokenValue': ''
    },
    ast.LShift: {
        'tokenValue': ''
    },
    ast.RShift: {
        'tokenValue': ''
    },
    ast.BitOr: {
        'tokenValue': ''
    },
    ast.BitXor: {
        'tokenValue': ''
    },
    ast.BitAnd: {
        'tokenValue': ''
    },
    ast.FloorDiv: {
        'tokenValue': ''
    },
    ast.unaryop: {
        'tokenValue': ''
    },
    ast.Invert: {
        'tokenValue': ''
    },
    ast.Not: {
        'tokenValue': 'not '
    },
    ast.UAdd: {
        'tokenValue': ''
    },
    ast.USub: {
        'tokenValue': ''
    },
    ast.cmpop: {
        'tokenValue': ''
    },
    ast.Eq: {
        'tokenValue': ' == '
    },
    ast.NotEq: {
        'tokenValue': ' != '
    },
    ast.Lt: {
        'tokenValue': ' < '
    },
    ast.LtE: {
        'tokenValue': ' <= '
    },
    ast.Gt: {
        'tokenValue': ' > '
    },
    ast.GtE: {
        'tokenValue': ' >= '
    },
    ast.Is: {
        'tokenValue': ' is '
    },
    ast.IsNot: {
        'tokenValue': ' is not '
    },
    ast.In: {
        'tokenValue': 'in '
    },
    ast.NotIn: {
        'tokenValue': 'not in '
    },
    ast.comprehension: {
        'tokenValue': '',
        'target':{
            'open': '',
            'close': ''
        },
        'iter':{
            'open': '',
            'close': ''
        },
        'ifs':{
            'open': '',
            'close': ''
        },
        'is_async':{
            'open': '',
            'close': ''
        }
    },
    ast.excepthandler: {
        'tokenValue': ''
    },
    ast.ExceptHandler: {
        'tokenValue': '',
        'type':{
            'open': '',
            'close': ''
        },
        'name':{
            'open': '',
            'close': ''
        },
        'body':{
            'open': '',
            'close': ''
        }
    },
    ast.arguments: {
        'tokenValue': '',
        'posonlyargs':{
            'open': '',
            'close': ''
        },
        'args':{
            'open': '',
            'close': ''
        },
        'vararg':{
            'open': '',
            'close': ''
        },
        'kwonlyargs':{
            'open': '',
            'close': ''
        },
        'kw_defaults':{
            'open': '',
            'close': ''
        },
        'kwarg':{
            'open': '',
            'close': ''
        },
        'defaults':{
            'open': ' = ',
            'close': ''
        }
    },
    ast.arg: {
        'tokenValue': '',
        'arg':{
            'open': '',
            'close': ''
        },
        'annotation':{
            'open': '',
            'close': ''
        },
        'type_comment':{
            'open': '',
            'close': ''
        }
    },
    ast.keyword: {
        'tokenValue': '',
        'arg':{
            'open': '',
            'close': ''
        },
        'value':{
            'open': '',
            'close': ''
        }
    },
    ast.alias: {
        'tokenValue': '',
        'name':{
            'open': '',
            'close': ''
        },
        'asname':{
            'open': ' as ',
            'close': ''
        }
    },
    ast.withitem: {
        'tokenValue': '',
        'context_expr':{
            'open': '',
            'close': ''
        },
        'optional_vars':{
            'open': '',
            'close': ''
        }
    },
    ast.match_case: {
        'tokenValue': '',
        'pattern':{
            'open': '',
            'close': ''
        },
        'guard':{
            'open': '',
            'close': ''
        },
        'body':{
            'open': '',
            'close': ''
        }
    },
    ast.pattern: {
        'tokenValue': ''
    },
    ast.MatchValue: {
        'tokenValue': '',
        'value':{
            'open': '',
            'close': ''
        }
    },
    ast.MatchSingleton: {
        'tokenValue': '',
        'value':{
            'open': '',
            'close': ''
        }
    },
    ast.MatchSequence: {
        'tokenValue': '',
        'patterns':{
            'open': '',
            'close': ''
        }
    },
    ast.MatchMapping: {
        'tokenValue': '',
        'keys':{
            'open': '',
            'close': ''
        },
        'patterns':{
            'open': '',
            'close': ''
        },
        'rest':{
            'open': '',
            'close': ''
        }
    },
    ast.MatchClass: {
        'tokenValue': '',
        'cls':{
            'open': '',
            'close': ''
        },
        'patterns':{
            'open': '',
            'close': ''
        },
        'kwd_attrs':{
            'open': '',
            'close': ''
        },
        'kwd_patterns':{
            'open': '',
            'close': ''
        }
    },
    ast.MatchStar: {
        'tokenValue': '',
        'name':{
            'open': '',
            'close': ''
        }
    },
    ast.MatchAs: {
        'tokenValue': '',
        'pattern':{
            'open': '',
            'close': ''
        },
        'name':{
            'open': '',
            'close': ''
        }
    },
    ast.MatchOr: {
        'tokenValue': '',
        'patterns':{
            'open': '',
            'close': ''
        }
    },
    ast.type_ignore: {
        'tokenValue': ''
    },
    ast.TypeIgnore: {
        'tokenValue': '',
        'lineno':{
            'open': '',
            'close': ''
        },
        'tag':{
            'open': '',
            'close': ''
        }
    },
    ast.slice: {
        'tokenValue': ''
    },
    ast.Index: {
        'tokenValue': ''
    },
    ast.ExtSlice: {
        'tokenValue': ''
    }
}

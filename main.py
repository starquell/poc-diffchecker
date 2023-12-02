import tree_sitter as ts
import sys

ts.Language.build_library(
    "build/my-languages.so",   ## shared library with compiled parsers
    ["grammars/go"],  ## paths to parser repositories
)

GO_LANGUAGE = ts.Language("build/my-languages.so", "go")

parser = ts.Parser()
parser.set_language(GO_LANGUAGE)
## TODO: auto-detect language from file extension. Extension is not always reliable, but for now it'll be fine.

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <filename>")
        sys.exit(1)
    
    with open(sys.argv[1], 'rb') as example:
        tree = parser.parse(example.read())
        print(f"Tree: {tree.root_node.sexp()}")

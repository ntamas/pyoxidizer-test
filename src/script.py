from rich import print

def fancy_test_func():
    """This is a docstring that should be stripped away by PyOxidizer. Grep for
    'no_it_has_not_been_stripped_away' in the output of `strings` on the final
    executable to verify.

    Also grep for 'fancy_test_func' to verify that the source code was _not_
    included in the output.
    """
    return "test script"


print("This is a", fancy_test_func())
print("[green][bold]Success![/green][/bold]")

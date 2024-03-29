from ipywidgets import Output, Box, VBox, HBox, Label, Layout, Button
from IPython.display import display
import clipboard


class Navigator:
    """Navigator allows for selecting sympy subexpressions graphically.
    """

    def __init__(self):
        # A path is a list of indices for the args tuples of some
        # sympy expression ([1, 0, 2] => expr.args[1].args[0].args[2]
        self._current_path = []
        self._current_subexpr = None
        self._widgets = []
        self._expr = None

    def navigate(self, expr):
        """Open the Jupyter widgets to select a subexpression graphically.

        Parameters
        ----------
        expr: sympy expression
            The sympy expression from which to select a subexpression.

        """
        self._expr = expr
        self._current_subexpr = expr
        self.show()

    def show(self):
        """Build and update the GUI"""
        for w in self._widgets:
            w.close()

        self._widgets = []

        label = Label(value='Current selection:')
        expr_output = Output()
        with expr_output:
            display(self._current_subexpr)
        up_button = Button(description='Go Up')
        up_button.on_click(self.handle_up)
        copy_path_button = Button(description='Copy Path')
        copy_path_button.on_click(self.handle_copy_path)
        self.msg_output = Output()
        hbox = HBox([up_button, copy_path_button])
        vbox = VBox([label, expr_output, hbox, self.msg_output],
                    layout=Layout(border='solid 2px grey',
                                  padding='5px'
                                  ))
        display(vbox)
        self._widgets.append(vbox)

        if not self._current_subexpr.args:
            return

        label = Label(value='Subexpressions:')
        rows = [label]
        for i, arg in enumerate(self._current_subexpr.args):
            output = Output()
            with output:
                display(arg)
            button = Button(description='Select')
            button.on_click(self.handle_select)
            button.iarg = i
            hbox = HBox([output, button])
            rows.append(hbox)
        box = VBox(rows, layout=Layout(border='dashed 2px grey', padding='5px'))
        display(box)
        self._widgets.append(box)

    def handle_select(self, event):
        """Event handler for when a "Select" button was clicked"""
        self._current_path.append(event.iarg)
        self._current_subexpr = get_by_path(self._expr, self._current_path)
        self.show()

    def handle_up(self, event):
        """Event handler for when the "Go up" button was clicked"""
        if len(self._current_path) == 0:
            return
        self._current_path.pop()
        self._current_subexpr = get_by_path(self._expr, self._current_path)
        self.show()

    def handle_copy_path(self, event):
        """Event handler for when the "Copy" button was clicked"""

        path = []
        for part in self._current_path:
            path.append('/[%d]' % part)

        clipboard.copy('"' + path + '"')
        with self.msg_output:
            print('Path copied to clipboard')



def get_by_path(expr, path):
    """ Retrieve a subexpression by giving its path

    Parameters
    ----------
    expr: sympy expression
        The expression from which to retrieve the subexpression.
    path: list of ints or EPath string
        The indices of the args tuples, see example.

    Returns
    -------
    sympy expression for given path


    Examples
    --------
    >>> get_by_path(expr, [1, 0, 3, 1])
       is equivalent to
    >>> expr.args[1].args[0].args[3].args[1]

    """

    if isinstance(path, str):
        path_ = []
        for part in path.split('/'):
            part = part.replace('[', '').replace(']', '')
            path_.append(int(part))
        path = path_

    subexpr = expr
    for idx in path:
        subexpr = subexpr.args[idx]
    return subexpr

# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1089_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 611 bytes
import dash
from dash import html, dcc
app = dash.Dash(__name__)

@app.callback(dash.dependencies.Output("output", "children"), [
 dash.dependencies.Input("input", "value")])
def update_output(value):
    return html.A("Click here", href=value)


app.layout = html.Div([
 dcc.Input(id="input", type="text", placeholder="Enter URL"),
 html.Div(id="output")])
if __name__ == "__main__":
    app.run_server(debug=True)

# okay decompiling 1089_1.pyc

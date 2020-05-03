# Decorators

#@app.route('/contact') # browsed from url /contact it returns specified
#template
#def contact():
#    return render_template('contact.html')
from functools import wraps

def add_wrapping_with_style(style, style1):

    def add_wrapping(item):
        @wraps(item)
        def wrapped_item():
            return 'a {} and {} wrapped up box of {}'.format(style, style1, str(item()))
        return wrapped_item # wrapped_item() throws an error
    return add_wrapping

#@add_wrapping
@add_wrapping_with_style('Beautiful ', 'ss')
def new_gpu():
    return 'A new high end GPU'

print(new_gpu())

print(new_gpu.__name__)

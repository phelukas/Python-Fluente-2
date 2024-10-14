def tag(name, *content, class_=None, **attrs):
    """Generate one or more HTML tags"""
    # Print dos parâmetros para acompanhar cada chamada
    print("\n")
    print(f"name: {name}")
    print(f"content: {content}")
    print(f"class_: {class_}")
    print(f"attrs: {attrs}")
    print("\n")
    # Restante da função
    if class_ is not None:
        attrs["class"] = class_
    attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = "".join(attr_pairs)
    if content:
        elements = (f"<{name}{attr_str}>{c}</{name}>" for c in content)
        return "\n".join(elements)
    else:
        return f"<{name}{attr_str} />"


tag("br")
"<br />"

tag("p", "hello")
"<p>hello</p>"

print(tag("p", "hello", "world"))
"<p>hello</p>"
"<p>world</p>"

tag("p", "hello", id=33)
'<p id="33">hello</p>'

print(tag("p", "hello", "world", class_="sidebar"))
'<p class="sidebar">hello</p>'
'<p class="sidebar">world</p>'

tag(content="testing", name="img")
'<img content="testing" />'

my_tag = {
    "name": "img",
    "title": "Sunset Boulevard",
    "src": "sunset.jpg",
    "class": "framed",
}

tag(**my_tag)
'<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'


###### Parâmetros somente posicionais  ##########


def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


f(10, 20, 30, d=40, e=50, f=60)

f(10, b=20, c=30, d=40, e=50, f=60)  # b cannot be a keyword argument
f(10, 20, 30, 40, 50, f=60)  # e must be a keyword argument


def divmod(a, b, /):
    """
    Recebe dois números (não complexos) como argumentos e retorna um par de
    números que consiste em seu quociente e resto ao usar a divisão inteira.
    """
    return (a // b, a % b)

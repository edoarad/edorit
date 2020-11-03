# HatunHackathon
See https://docs.google.com/presentation/d/1rznXBWn9Fd3MhqTOP81x0gXLR_0CuPeuJ_pSeJJmoTU/edit and join us at the discord channel.

# General
Write something here.

# Getting Started
Install python 3 on your computer, and clone this repository.
Then follow the explanation for your operating system.
In the end your web server is running on port 8000, so you should be able to browse it at:
```
http://127.0.0.1:8000/
```

## Windows
Open cmd __in this folder__.
To install all requirements execute:
```
scripts\install.bat
```
To run the web server execute:
```
scripts\run-website.bat
```

## Linux
Open cmd __in the scripts folder__.
To install all requirements execute:
```
install.sh
```
To run the web server execute:
```
run-website.sh
```

## Adding React

If you know React — you know it's amazing for creating interactive javascript widgets, so here's
an easy way to embed it in the project.

Let's say you're working on page A, and your template is `templates/a.pug`. To add a react
component, you need to:

1. Add a script — for example, `static/example.js` — with a React class — for example, `Example`.

   (This file actually exists as a reference, in case you want to check it out.)

2. In your template, import it using the `{% react_import '<filename>' %}` tag — so in our example,
   `{% react_import 'example.js' %}`.

3. Finally, to render your component unto some element, use the `{% react '<Component>' '<selector>' %}
   — in our example, that'd be `{% react 'Example' '#example' %}`, which would load us unto the `<div id="exmaple">`.

   This tag actually has to be closed with the `{% endreact %}` tag; between them, you can pass props
   to your component like so:

   ```
   {% react '<Component>' '<selector>' %}
   script.
       var props = {...}
   {% endreact %}
   ```

   For example:

   ```
   {% react 'Example' '#example' %}
   script.
       var props = {message: 'Hello, world!'}
   {% endreact %}
   ```

   Is akin to `ReactDOM.render(<Example message="Hello, world!" />)`.

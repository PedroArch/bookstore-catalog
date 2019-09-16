
# CATALOG PROJECT - Udacity Full Stack Web Developer Nanodegree

> A Web Catalog with CRUD Features

![](screen-shot.png)

For this project, my task was to create a web catalog that has CRUD tools. In addition, the catalog has a login system using Google's authentication
and authorization system.


###### _[PROJECT RUBRICS](project-rubrics.md)_
###### _[PROJECT DESCRIPTION](project-description.md)_

## Requirements

- Python 2.7
- flask
- sqlalchemy
- Winzip or 7-zip

_You can use a virtual machine given in development setup session_

## Development setup

1. To have the same environment that this project was developed on, I recommend use a virtual machine.

2. Download and install [Vagrant](https://www.vagrantup.com/)

3. Download and install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)

4. Clone this repo https://github.com/udacity/fullstack-nanodegree-vm.git

5. At terminal in the folder with `vagrantfile` type, to bring the virtual machine online:
```sh
vagrant up
```

## Running the program

1. Clone this project to catalog folder

2. Run in your terminal ```python database_setup.py ```

3. Run in your terminal to init a database exemple ```python lotsofbooks.py ```

4. Run in your terminal  ```python application.py```

5. Open your browser set URL http://localhost:8000

## Usage example

When you run the program the web server comes online to use all its CRUD, login and logout functions.

_If you find some bugs, problems you can send a message to me [twitter] or [email]._

## Release History

* 0.0.1
   * First version

## Meta

Pedro Carvalho – [@PedrArch](https://twitter.com/PedroArch) – pedrofrancocarvalho@gmail.com

[https://github.com/PedroArch](https://github.com/PedroArch/)

## Contributing

1. Fork it (<https://github.com/PedroArch/bookstore-catalog/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[twitter]:https://twitter.com/PedroArch
[github]:https://github.com/PedroArch
[email]: pedrofrancocarvalho@gmail.com

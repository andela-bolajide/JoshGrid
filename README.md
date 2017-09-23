[![Build Status](https://travis-ci.org/BolajiOlajide/JoshGrid.svg?branch=develop)](https://travis-ci.org/BolajiOlajide/JoshGrid)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Coverage Status](https://coveralls.io/repos/github/andela-bolajide/JoshGrid/badge.svg?branch=develop)](https://coveralls.io/github/andela-bolajide/JoshGrid?branch=develop)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/andela-bolajide/JoshGrid/badges/quality-score.png?b=develop)](https://scrutinizer-ci.com/g/andela-bolajide/JoshGrid/?branch=develop)
[![CircleCI](https://circleci.com/gh/BolajiOlajide/JoshGrid.svg?style=svg)](https://circleci.com/gh/BolajiOlajide/JoshGrid)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/758b040267914a11828fdb89fd333d97)](https://www.codacy.com/app/andela-bolajide/JoshGrid?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andela-bolajide/JoshGrid&amp;utm_campaign=Badge_Grade)
[![Python 3](https://pyup.io/repos/github/BolajiOlajide/JoshGrid/python-3-shield.svg)](https://pyup.io/repos/github/BolajiOlajide/JoshGrid/)
[![Updates](https://pyup.io/repos/github/BolajiOlajide/JoshGrid/shield.svg)](https://pyup.io/repos/github/BolajiOlajide/JoshGrid/)

# JoshGrid

This repository contains the backend and frontend of a MAIL-sending application. It is basically an API which is accessible to the outside world once they have an account and have been authenticated.

## Project Dependencies

### Frontend Dependencies

- [axios](https://github.com/mzabriskie/axios) - Promise based HTTP client for the browser and node.js
- [babel-cli](https://babeljs.io/docs/usage/cli/) - Allows running the app in ES6 mode on the fly without having to transpile down to ES5
- [babel-core](https://www.npmjs.com/package/babel-core) - Babel compiler core
- [babel-loader](), [css-loader](), [file-loader](), [style-loader]() - Loaders to be used with webpack for ES6 transpiling and CSS loading.
- [babel-preset-es2015](https://babeljs.io/docs/plugins/preset-es2015/), [babel-preset-stage-0](https://babeljs.io/docs/plugins/preset-stage-0/), [babel-preset-react](http://babeljs.io/docs/plugins/preset-react/), [babel-register](https://babeljs.io/docs/usage/babel-register/) - These packages provide Babel presets for es2015 plugins, stage 0 plugins and react plugins.
- [compression](https://www.npmjs.com/package/compression) - Node.js compression middleware.
- [dotenv](https://www.npmjs.com/package/dotenv) - a zero-dependency module that loads environment variables from a .env file.
- [express](https://expressjs.com/) - Fast, unopinionated, minimalist web framework for Node.js.
- [enzyme](http://airbnb.io/enzyme/) - JavaScript Testing utilities for React
- [jsdom](https://github.com/tmpvar/jsdom) - A JavaScript implementation of the WHATWG DOM and HTML standards, for use with node.js
- [mocha](https://mochajs.org/) - a feature-rich JavaScript test framework running on Node.js and in the browser, making asynchronous testing simple and fun.
- [prop-types](https://facebook.github.io/react/docs/typechecking-with-proptypes.html) - used for typechecking react components' props.
- [react](https://facebook.github.io/react/) - a javascript library for building user interfaces.
- [react-dom](https://facebook.github.io/react/docs/react-dom.html) - provides DOM-specific methods that can be used at the top level of your app and as an escape hatch to get outside of the React model if you need to.
- [react-router](https://reacttraining.com/react-router/), [react-router-dom](https://reacttraining.com/react-router/) - Declarative routing for React
- [toastr](https://codeseven.github.io/toastr/) -  a Javascript library for Gnome / Growl type non-blocking notifications.
- [webpack](https://webpack.js.org/) - a module bundler.

### Backend Dependencies
- [Celery](http://www.celeryproject.org/) - Celery is an asynchronous task queue/job queue based on distributed message passing.
- [Cloudinary](http://cloudinary.com/) - Seamlessly manage your website's images in the cloud - image upload, cloud storage, image manipulation, image API and fast CDN.
- [Coverage.py](https://coverage.readthedocs.io/en/coverage-4.4.1/) - a tool for measuring code coverage of Python programs. It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not.
- [Coveralls](https://pypi.python.org/pypi/coveralls) - Show coverage stats online via coveralls.io
- [Django](https://www.djangoproject.com/) - a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel.
- [Django-anymail](https://anymail.readthedocs.io/en/stable/) - Django email backends and webhooks for Mailgun, Mailjet, Postmark, SendGrid, SparkPost and more
- [Django-Celery-Beat](https://github.com/celery/django-celery-beat) - Celery Periodic Tasks backed by the Django ORM
- [Django-Celery-Results](http://django-celery-results.readthedocs.io/en/latest/) - This extension enables you to store Celery task results using the Django ORM.
- [DjangoRestFramework](http://www.django-rest-framework.org/) - a powerful and flexible toolkit for building Web APIs
- [gunicorn](http://gunicorn.org/) - a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model.
- [iPython](https://ipython.org/install.html) - a command shell for interactive computing in multiple programming languages.
- [psycopg2](http://initd.org/psycopg/) - the most popular PostgreSQL adapter for the Python programming language.
- [python-env](https://pypi.python.org/pypi/python-env/1.0.0) - Get and Set environment variables using .env file

## Installation

To install `JoshGrid`, do the following:
- Clone the project from github with the command `git clone https://github.com/BolajiOlajide/JoshGrid`
- Install Redis with `brew install redis` on OSX or checkout the [docs](https://redis.io/) for how to install on other OS.

## Testing
The project is divided into frontend (React) and backend (Django) and it was developed using TDD (Test-Driven development) methodology.
A shell script is available for running the test, which is easy to use with the command `./run-test.sh`.
You can specify if you want to run backend test with the command `./run-test.sh backend` or frontend tests with the command `./run-test.sh frontend`

### Author
- [Bolaji Olajide](https://twitter.com/Bolaji___)

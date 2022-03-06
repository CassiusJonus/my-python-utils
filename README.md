# Custom Utilities

## Description

This package contains some utility modules that can be used in other projects. Currently,

## Sections

1. [Included Modules](#included-modules)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [License](#license)

## Included modules

### message_notifier

Allows a user to send an email or a text message including a subject and a body.
The username and password of the sender's email account as well as the smtp
server and port can be configured in a .env file, which will be accessed using
dotenv-python.

## Requirements

The following packages are required to use this package:

- smtplib
- email
- dotenv-python

## Usage

### Setup

Use `pip install custom-utils-cassius-jonus` to install the package and import
the package using `import custom_utils`. If you want to import a specif module,
use `from custom_utils import <module_name>`.

If you want to use the message_notifier module, you should use a .env file to store the credentials
for the email account that will be sending notifications.

## License

This project uses the MIT License. The license text can be found [here](/LICENSE).

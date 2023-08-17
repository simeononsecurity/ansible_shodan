# Ansible Shodan Modules

![Ansible](https://img.shields.io/badge/ansible-2.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
[![Ansible Galaxy](https://github.com/simeononsecurity/ansible_shodan/actions/workflows/ansible_galaxy_collection.yml/badge.svg)](https://github.com/simeononsecurity/ansible_shodan/actions/workflows/ansible_galaxy_collection.yml)

This collection provides Ansible modules for interacting with the Shodan API. The modules allow you to perform various tasks related to Shodan, such as querying information, searching for hosts, and more.

## Modules

This collection includes the following modules:

- [`get_shodan_api_info`](https://github.com/simeononsecurity/ansible_shodan/blob/main/collections/ansible_collections/simeononsecurity/shodan/plugins/modules/get_shodan_api_info.py): Returns information about the API plan linked to the given API key.
- [`get_shodan_client_http_headers`](https://github.com/simeononsecurity/ansible_shodan/blob/main/collections/ansible_collections/simeononsecurity/shodan/plugins/modules/get_shodan_client_http_headers.py): Shows the HTTP headers that your client sends when connecting to a web server.
- [`get_shodan_client_ip`](https://github.com/simeononsecurity/ansible_shodan/blob/main/collections/ansible_collections/simeononsecurity/shodan/plugins/modules/get_shodan_client_ip.py): Get your current IP address as seen from the Internet.
- See more at the [modules directory..](https://github.com/simeononsecurity/ansible_shodan/tree/main/collections/ansible_collections/simeononsecurity/shodan/plugins/modules)


## Installation

You can install this collection using the following command:

```bash
ansible-galaxy collection install simeononsecurity.ansible_shodan
```

See the collection on the [Ansible Galaxy](https://galaxy.ansible.com/simeononsecurity/ansible_shodan) page.

## Usage
To use these modules, include them in your Ansible playbooks or roles and reference them using their respective names. Here's an example playbook using the `get_shodan_api_info` module:
```yml
---
- name: Get Shodan API Info
  hosts: localhost
  tasks:
    - name: Get Shodan API Info
      simeononsecurity.ansible_shodan.get_shodan_api_info:
        api_key: your_shodan_api_key
      register: shodan_api_info

    - name: Display API Info
      debug:
        var: shodan_api_info
```

## Contributing
Contributions to this collection are welcome! If you have improvements or new modules to add, please fork this repository, create a new branch, and submit a pull request.

## License
This project is licensed under the MIT License. See the [`LICENSE`](https://github.com/simeononsecurity/ansible_shodan/blob/main/LICENSE) file for details.

## Author
This Ansible Shodan Modules collection is authored by [SimeonOnSecurity](https://simeononsecurity.ch/).

## Acknowledgments
Special thanks to the Shodan API for providing the capabilities to interact with their service using Ansible.

## Alternate Versions
If you need a version in powershell, we have our [Shodan Powershell repo](https://github.com/simeononsecurity/Shodan_PS).
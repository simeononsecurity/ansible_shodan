#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests

def get_shodan_dns_domain(api, domain):
    api_string = f"?key={api}"
    if not api:
        return "Please set the 'api' variable to your Shodan API key."
    elif not domain:
        return "Please specify a domain address using the 'domain' parameter."
    else:
        response = requests.get(f"https://api.shodan.io/dns/domain/{domain}{api_string}")
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed to retrieve DNS domain information. Status code: {response.status_code}"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            api=dict(required=False, type='str'),
            domain=dict(required=True, type='str')
        )
    )

    api_key = module.params['api']
    domain = module.params['domain']
    result = get_shodan_dns_domain(api_key, domain)
    module.exit_json(changed=False, result=result)

if __name__ == '__main__':
    main()

#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests

def get_shodan_dns_resolve(api, domains):
    api_string = f"&key={api}"
    if not api:
        return "Please set the 'api' variable to your Shodan API key."
    elif not domains:
        return "Please specify one or more domain addresses using the 'domains' parameter."
    else:
        response = requests.get(f"https://api.shodan.io/dns/resolve?hostnames={domains}{api_string}")
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed to resolve DNS domains. Status code: {response.status_code}"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            api=dict(required=False, type='str'),
            domains=dict(required=True, type='str')
        )
    )

    api_key = module.params['api']
    domains = module.params['domains']
    result = get_shodan_dns_resolve(api_key, domains)
    module.exit_json(changed=False, result=result)

if __name__ == '__main__':
    main()

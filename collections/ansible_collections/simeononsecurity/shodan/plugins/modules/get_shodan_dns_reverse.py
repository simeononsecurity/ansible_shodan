#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests

def get_shodan_dns_reverse(api, ips):
    api_string = f"&key={api}"
    if not api:
        return "Please set the 'api' variable to your Shodan API key."
    elif not ips:
        return "Please specify IP addresses using the 'ips' parameter."
    else:
        response = requests.get(f"https://api.shodan.io/dns/reverse?ips={ips}{api_string}")
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed to perform DNS reverse lookup. Status code: {response.status_code}"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            api=dict(required=False, type='str'),
            ips=dict(required=True, type='str')
        )
    )

    api_key = module.params['api']
    ips = module.params['ips']
    result = get_shodan_dns_reverse(api_key, ips)
    module.exit_json(changed=False, result=result)

if __name__ == '__main__':
    main()

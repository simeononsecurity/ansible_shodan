#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests

def set_shodan_scan_ip(api, ips):
    api_string = f"?key={api}"
    
    if not api:
        return "Please set the 'api' variable to your Shodan API key."
    else:
        ip_string = f"&ips={ips}"
        response = requests.post(f"https://api.shodan.io/shodan/scan{api_string}{ip_string}")
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed to initiate Shodan IP scan. Status code: {response.status_code}"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            api=dict(required=False, type='str'),
            ips=dict(required=True, type='str')
        )
    )

    api_key = module.params['api']
    ips_to_scan = module.params['ips']
    result = set_shodan_scan_ip(api_key, ips_to_scan)
    module.exit_json(changed=False, result=result)

if __name__ == '__main__':
    main()

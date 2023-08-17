#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests

def get_shodan_scan_id(api, scan_id):
    api_string = f"?key={api}"
    
    if not api:
        return "Please set the 'api' variable to your Shodan API key."
    else:
        if not scan_id:
            return "Please specify a Shodan Scan ID with -ID [string]"
        else:
            response = requests.get(f"https://api.shodan.io/shodan/scan/{scan_id}{api_string}")
            if response.status_code == 200:
                return response.json()
            else:
                return f"Failed to get Shodan scan status. Status code: {response.status_code}"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            api=dict(required=False, type='str'),
            id=dict(required=True, type='str')
        )
    )

    api_key = module.params['api']
    scan_id = module.params['id']
    result = get_shodan_scan_id(api_key, scan_id)
    module.exit_json(changed=False, result=result)

if __name__ == '__main__':
    main()

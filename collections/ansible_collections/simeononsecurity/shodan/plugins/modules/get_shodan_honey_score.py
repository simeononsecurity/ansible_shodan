#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests

def get_shodan_honey_score(api, ip):
    api_string = f"?key={api}"
    if not api:
        return "Please set the 'api' variable to your Shodan API key."
    elif not ip:
        return "Please specify an IP address using the 'ip' parameter."
    else:
        response = requests.get(f"https://api.shodan.io/labs/honeyscore/{ip}{api_string}")
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed to get honey score. Status code: {response.status_code}"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            api=dict(required=False, type='str'),
            ip=dict(required=True, type='str')
        )
    )

    api_key = module.params['api']
    ip = module.params['ip']
    result = get_shodan_honey_score(api_key, ip)
    module.exit_json(changed=False, result=result)

if __name__ == '__main__':
    main()

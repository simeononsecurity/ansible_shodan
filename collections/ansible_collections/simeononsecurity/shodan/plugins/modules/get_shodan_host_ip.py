#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests

def get_shodan_host_ip(api, ip, minify):
    api_string = f"?key={api}"
    minify_string = f"&minify={minify}"
    
    if not api:
        return "Please set the 'api' variable to your Shodan API key."
    elif not ip:
        return "Please specify an IP address using the 'ip' parameter."
    else:
        response = requests.get(f"https://api.shodan.io/shodan/host/{ip}{api_string}{minify_string}")
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed to get host information. Status code: {response.status_code}"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            api=dict(required=False, type='str'),
            ip=dict(required=True, type='str'),
            minify=dict(required=False, type='bool', default=True)
        )
    )

    api_key = module.params['api']
    ip = module.params['ip']
    minify = module.params['minify']
    result = get_shodan_host_ip(api_key, ip, minify)
    module.exit_json(changed=False, result=result)

if __name__ == '__main__':
    main()

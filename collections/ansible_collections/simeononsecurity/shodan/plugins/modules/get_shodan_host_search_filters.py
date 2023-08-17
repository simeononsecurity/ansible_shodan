#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests

def get_shodan_host_search_filters(api):
    api_string = f"?key={api}"
    
    if not api:
        return "Please set the 'api' variable to your Shodan API key."
    else:
        response = requests.get(f"https://api.shodan.io/shodan/host/search/filters{api_string}")
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed to get host search filters. Status code: {response.status_code}"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            api=dict(required=False, type='str')
        )
    )

    api_key = module.params['api']
    result = get_shodan_host_search_filters(api_key)
    module.exit_json(changed=False, result=result)

if __name__ == '__main__':
    main()

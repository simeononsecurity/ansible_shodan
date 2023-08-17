#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import requests

def get_shodan_host_search(api, query, facet, minify):
    api_string = f"?key={api}"
    query_string = f"&query={query}"
    minify_string = f"&minify={minify}"
    facet_string = f"&facet={facet}" if facet else ""
    
    if not api:
        return "Please set the 'api' variable to your Shodan API key."
    elif not query:
        return "Please specify your query using the 'query' parameter."
    else:
        response = requests.get(f"https://api.shodan.io/shodan/host/search{api_string}{query_string}{facet_string}{minify_string}")
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed to get host search results. Status code: {response.status_code}"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            api=dict(required=False, type='str'),
            query=dict(required=True, type='str'),
            facet=dict(required=False, type='str'),
            minify=dict(required=False, type='bool', default=True)
        )
    )

    api_key = module.params['api']
    query = module.params['query']
    facet = module.params['facet']
    minify = module.params['minify']
    result = get_shodan_host_search(api_key, query, facet, minify)
    module.exit_json(changed=False, result=result)

if __name__ == '__main__':
    main()

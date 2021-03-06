# esp_sdk.CustomSignatureResultsApi

All URIs are relative to https://api.evident.io

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](CustomSignatureResultsApi.md#create) | **POST** /api/v2/custom_signature_results.json_api | Create a(n) Custom Signature Result
[**list**](CustomSignatureResultsApi.md#list) | **PUT** /api/v2/custom_signature_results.json_api | Get a list of Custom Signature Results
[**list_alerts**](CustomSignatureResultsApi.md#list_alerts) | **GET** /api/v2/custom_signature_results/{custom_signature_result_id}/alerts.json_api | Returns the Alerts for a given Custom Signature Result
[**show**](CustomSignatureResultsApi.md#show) | **GET** /api/v2/custom_signature_results/{id}.json_api | Show a single Custom Signature Result


# **create**
> CustomSignatureResult create(code, custom_signature_definition_id, external_account_id, language, include=include, region=region, region_id=region_id)

Create a(n) Custom Signature Result



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureResultsApi()
code = 'code_example' # str | The code for this definition
custom_signature_definition_id = 56 # int | ID of the custom signature definition this result belongs to
external_account_id = 56 # int | ID of the external account the code should run for
language = 'language_example' # str | The language of the definition. Valid values are ruby, javascript
include = 'include_example' # str | Related objects that can be included in the response:  external_account, region, definition See Including Objects for more information. (optional)
region = 'region_example' # str | Code of the region the result code should run for. Ex: us-east-1. This can be sent instead of region_id (optional)
region_id = 56 # int | ID of the region the code should run for.  Required if region is not supplied. (optional)

try: 
    # Create a(n) Custom Signature Result
    api_response = api_instance.create(code, custom_signature_definition_id, external_account_id, language, include=include, region=region, region_id=region_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureResultsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code for this definition | 
 **custom_signature_definition_id** | **int**| ID of the custom signature definition this result belongs to | 
 **external_account_id** | **int**| ID of the external account the code should run for | 
 **language** | **str**| The language of the definition. Valid values are ruby, javascript | 
 **include** | **str**| Related objects that can be included in the response:  external_account, region, definition See Including Objects for more information. | [optional] 
 **region** | **str**| Code of the region the result code should run for. Ex: us-east-1. This can be sent instead of region_id | [optional] 
 **region_id** | **int**| ID of the region the code should run for.  Required if region is not supplied. | [optional] 

### Return type

[**CustomSignatureResult**](CustomSignatureResult.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedCollection list(include=include, filter=filter, page=page)

Get a list of Custom Signature Results



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureResultsApi()
include = 'include_example' # str | Related objects that can be included in the response:  external_account, region, definition See Including Objects for more information. (optional)
filter = {'key': 'filter_example'} # dict(str, str) | Filter Params for Searching.  Equality Searchable Attributes: [id, language, status]   Sortable Attribute: [id] Searchable Associations: [definition, region, external_account] See Searching Lists for more information. See the filter parameter of the association's list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Get a list of Custom Signature Results
    api_response = api_instance.list(include=include, filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureResultsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Related objects that can be included in the response:  external_account, region, definition See Including Objects for more information. | [optional] 
 **filter** | [**dict(str, str)**](str.md)| Filter Params for Searching.  Equality Searchable Attributes: [id, language, status]   Sortable Attribute: [id] Searchable Associations: [definition, region, external_account] See Searching Lists for more information. See the filter parameter of the association&#39;s list action to see what attributes are searchable on each association. See Conditions on Relationships in Searching Lists for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alerts**
> PaginatedCollection list_alerts(custom_signature_result_id, include=include, page=page)

Returns the Alerts for a given Custom Signature Result

This format is slightly different than the standard alert format. A successful call to this API returns a list of alerts for the custom signature result identified by the custom_signature_result_id parameter.

### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureResultsApi()
custom_signature_result_id = 56 # int | Custom Signature Result ID
include = 'include_example' # str | Related objects that can be included in the response:  external_account, region, custom_signature See Including Objects for more information. (optional)
page = '{:number=>1,+:size=>20}' # str | Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. (optional) (default to {:number=>1,+:size=>20})

try: 
    # Returns the Alerts for a given Custom Signature Result
    api_response = api_instance.list_alerts(custom_signature_result_id, include=include, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureResultsApi->list_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_signature_result_id** | **int**| Custom Signature Result ID | 
 **include** | **str**| Related objects that can be included in the response:  external_account, region, custom_signature See Including Objects for more information. | [optional] 
 **page** | **str**| Page Number and Page Size.  Number is the page number of the collection to return, size is the number of items to return per page. | [optional] [default to {:number&#x3D;&gt;1,+:size&#x3D;&gt;20}]

### Return type

[**PaginatedCollection**](PaginatedCollection.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show**
> CustomSignatureResult show(id, include=include)

Show a single Custom Signature Result



### Example 
```python
from __future__ import print_statement
import time
import esp_sdk
from esp_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = esp_sdk.CustomSignatureResultsApi()
id = 56 # int | Custom Signature Result ID
include = 'include_example' # str | Related objects that can be included in the response:  external_account, region, definition See Including Objects for more information. (optional)

try: 
    # Show a single Custom Signature Result
    api_response = api_instance.show(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSignatureResultsApi->show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Custom Signature Result ID | 
 **include** | **str**| Related objects that can be included in the response:  external_account, region, definition See Including Objects for more information. | [optional] 

### Return type

[**CustomSignatureResult**](CustomSignatureResult.md)

### Authorization

See https://github.com/EvidentSecurity/esp-sdk-python#set-your-hmac-security-keys

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


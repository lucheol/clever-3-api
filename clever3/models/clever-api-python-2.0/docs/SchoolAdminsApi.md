# clever.SchoolAdminsApi

All URIs are relative to *https://api.clever.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_district_for_school_admin**](SchoolAdminsApi.md#get_district_for_school_admin) | **GET** /school_admins/{id}/district | 
[**get_school_admin**](SchoolAdminsApi.md#get_school_admin) | **GET** /school_admins/{id} | 
[**get_school_admins**](SchoolAdminsApi.md#get_school_admins) | **GET** /school_admins | 
[**get_schools_for_school_admin**](SchoolAdminsApi.md#get_schools_for_school_admin) | **GET** /school_admins/{id}/schools | 

# **get_district_for_school_admin**
> DistrictResponse get_district_for_school_admin(id)



Returns the district for a school admin

### Example
```python
from __future__ import print_function
import time
import clever
from clever.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = clever.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = clever.SchoolAdminsApi(clever.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_district_for_school_admin(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchoolAdminsApi->get_district_for_school_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DistrictResponse**](DistrictResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_admin**
> SchoolAdminResponse get_school_admin(id)



Returns a specific school admin

### Example
```python
from __future__ import print_function
import time
import clever
from clever.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = clever.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = clever.SchoolAdminsApi(clever.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_school_admin(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchoolAdminsApi->get_school_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SchoolAdminResponse**](SchoolAdminResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_admins**
> SchoolAdminsResponse get_school_admins(limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of school admins

### Example
```python
from __future__ import print_function
import time
import clever
from clever.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = clever.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = clever.SchoolAdminsApi(clever.ApiClient(configuration))
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try:
    api_response = api_instance.get_school_admins(limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchoolAdminsApi->get_school_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**SchoolAdminsResponse**](SchoolAdminsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schools_for_school_admin**
> SchoolsResponse get_schools_for_school_admin(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the schools for a school admin

### Example
```python
from __future__ import print_function
import time
import clever
from clever.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = clever.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = clever.SchoolAdminsApi(clever.ApiClient(configuration))
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try:
    api_response = api_instance.get_schools_for_school_admin(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchoolAdminsApi->get_schools_for_school_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**SchoolsResponse**](SchoolsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


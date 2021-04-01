# clever.SchoolsApi

All URIs are relative to *https://api.clever.com/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_district_for_school**](SchoolsApi.md#get_district_for_school) | **GET** /schools/{id}/district | 
[**get_school**](SchoolsApi.md#get_school) | **GET** /schools/{id} | 
[**get_schools**](SchoolsApi.md#get_schools) | **GET** /schools | 
[**get_sections_for_school**](SchoolsApi.md#get_sections_for_school) | **GET** /schools/{id}/sections | 
[**get_students_for_school**](SchoolsApi.md#get_students_for_school) | **GET** /schools/{id}/students | 
[**get_teachers_for_school**](SchoolsApi.md#get_teachers_for_school) | **GET** /schools/{id}/teachers | 

# **get_district_for_school**
> DistrictResponse get_district_for_school(id)



Returns the district for a school

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
api_instance = clever.SchoolsApi(clever.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_district_for_school(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchoolsApi->get_district_for_school: %s\n" % e)
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

# **get_school**
> SchoolResponse get_school(id)



Returns a specific school

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
api_instance = clever.SchoolsApi(clever.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_school(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchoolsApi->get_school: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SchoolResponse**](SchoolResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schools**
> SchoolsResponse get_schools(limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns a list of schools

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
api_instance = clever.SchoolsApi(clever.ApiClient(configuration))
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try:
    api_response = api_instance.get_schools(limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchoolsApi->get_schools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_sections_for_school**
> SectionsResponse get_sections_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the sections for a school

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
api_instance = clever.SchoolsApi(clever.ApiClient(configuration))
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try:
    api_response = api_instance.get_sections_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchoolsApi->get_sections_for_school: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**SectionsResponse**](SectionsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_students_for_school**
> StudentsResponse get_students_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the students for a school

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
api_instance = clever.SchoolsApi(clever.ApiClient(configuration))
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try:
    api_response = api_instance.get_students_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchoolsApi->get_students_for_school: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**StudentsResponse**](StudentsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teachers_for_school**
> TeachersResponse get_teachers_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)



Returns the teachers for a school

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
api_instance = clever.SchoolsApi(clever.ApiClient(configuration))
id = 'id_example' # str | 
limit = 56 # int |  (optional)
starting_after = 'starting_after_example' # str |  (optional)
ending_before = 'ending_before_example' # str |  (optional)

try:
    api_response = api_instance.get_teachers_for_school(id, limit=limit, starting_after=starting_after, ending_before=ending_before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchoolsApi->get_teachers_for_school: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 

### Return type

[**TeachersResponse**](TeachersResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


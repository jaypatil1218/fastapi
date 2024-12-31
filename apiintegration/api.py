from http.client import responses

import requests

endpoint="https://todo.pixegami.io/"


result=requests.get(endpoint)

data =result.json()

print(data)

endpoint_status=result.status_code

print(endpoint_status)

def test_api_status_endpoint():
    response=requests.get(endpoint)
    assert response.status_code==200



def test_create_task():
    payload={

            "content": "string",
            "user_id": "string",
            "task_id": "string",
            "is_done": False
        }

    res=requests.put(endpoint+"/create-task",json=payload)
    assert res.status_code==200
    print(res.json())
    data1=res.json()


    taskid=data1['task']['task_id']
    get_responses=requests.get(endpoint+f"/get-task/{taskid}")
    get_taskdata=get_responses.json()
   # assert  get_taskdata["content"]=="some other content"

    print("data: ",get_taskdata)

    payload={
  "content": "upfated string",
  "user_id": "ustring",
  "task_id": "ustring",
  "is_done": False }

    res_update=requests.put(endpoint+"/update-task",json=payload)
    print(res_update.json())
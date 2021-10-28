const HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}
const callApi = async (body) => {
    const bodyJson = JSON.stringify(body);
    const resp = await fetch('/graphql', {
        method: 'POST',
        headers: {...HEADERS},
        body: bodyJson
    });
    const data = await resp.json();
    return {...data}
}
const getTaskStatus = async () => {
    const query = `{
      taskStatus {
        value
        name
      }
    }
`
    const {data} = await callApi({
        query: query
    });
    const {taskStatus} = data;
    return [...taskStatus]
}

const updateTask = async (variables) => {
    const query = `    
        mutation($id:Int,$endTime:String,$status:String,$description:String,$pullRequest:String){
            updateTask(id:$id,endTime:$endTime,status:$status,description:$description,pullRequests:$pullRequest){
                ok,
                task{
                    id,
                    name,
                    description,
                    pullRequests
                }
            }
        }
  `;
    const {data} = await callApi({
        query: query,
        variables
    });
    return data;
}

export {
    getTaskStatus,
    updateTask
}
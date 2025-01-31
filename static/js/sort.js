function sortTasks(order) {
    fetch(`?order=${order}`)
    .then(response => response.text())
    .then(html => {
        console.log("Fetched HTML:", html);

        const parser = new DOMParser();
        const doc = parser.parseFromString(html, "text/html");

        const newTaskList = doc.getElementById("task-list");
        if (!newTaskList) {
            console.error("Error: #task-list not found in fetched HTML");
            return;
        }

        document.getElementById("task-list").innerHTML = newTaskList.innerHTML;
    })
    .catch(error => console.error("Error sorting tasks:", error));
}
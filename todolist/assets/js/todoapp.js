const todoURL = 'http://localhost:8000/apis/v1/';


var ul = document.getElementById('todolist');

const loadtodolist = async (url) => {
  const response = await fetch(url);
  const list = await response.json(); //extract JSON from the http response

  if (list){
    ul.innerHTML = '';    
    for(let i = 0; i < list.length; i++) {
      let obj = list[i];

      var deleteSpan = document.createElement("SPAN");
      var txt = document.createTextNode("\u00D7");
      deleteSpan.className = "close";
      deleteSpan.onclick = function() {
        var div = this.parentElement;
        div.style.display = "none";

        todoUpdate(todoURL + obj.id + '/', 'DELETE');
      }
      deleteSpan.appendChild(txt);

      var editSpan = document.createElement("SPAN");
      var txt = document.createTextNode("\u270E");
      editSpan.className = "edit";
     
      editSpan.onclick = function() {
        const update = $("#myModal > .modal-dialog > .modal-content > .modal-body > .updateToDo")[0];
        
        update.value = obj.title;
        update.id = obj.id;
        $("#myModal").modal('show');
      }
      editSpan.appendChild(txt);

      var li = document.createElement("li");
      li.appendChild(document.createTextNode(obj.title));

      li.className= 'todoapp';

      if(obj.done === true){
        li.className= 'todoapp checked';
      }

      li.id = obj.id;
      li.appendChild(editSpan);
      li.appendChild(deleteSpan);
      
      ul.appendChild(li);
    }
  }
}

const todoUpdate = async (url, requestType, payload=null) => {
  load = (payload !== null) ? JSON.stringify(payload): null;
  const response = await fetch(url, {
    method: requestType,
    body: load, // string or object
    headers: {
      'Content-Type': 'application/json'
    }
  });
 
  const todo = (response.status !== 204 ) ? await response.json() : null; //extract JSON from the http response
  
  if (todo){
    loadtodolist(todoURL);
  }
}

// Add a "checked" symbol when clicking on a list item
var list = document.querySelector('ul');
list.addEventListener('click', function(ev) {
  if (ev.target.tagName === 'LI') {
    const id = ev.target.id;
    let payload = {
      done: false
    };
    
    if (ev.target.className === 'todoapp'){
      payload.done = true;
    }

    url = todoURL + id + '/';
    todoUpdate(url, 'PATCH', payload);

    ev.target.classList.toggle('checked');
  }
}, false);

add = () => {
  const input = document.getElementById('newToDo');
  if (input.value.length == 0){
    document.getElementsByClassName('invalid-feedback')[0].style.display= 'block';
    return;
  }
  const payload = {
    title: input.value
  };

  input.value = '';

  todoUpdate(todoURL, 'POST', payload);
};

edit = () => {
  $("#myModal").modal('hide');

  const updateInput = $("#myModal > .modal-dialog > .modal-content > .modal-body > .updateToDo")[0];
        

  const url = todoURL + updateInput.id + '/';

  payload = {
    title: updateInput.value
  };

  todoUpdate(url, 'PUT', payload);
}

loadtodolist(todoURL);
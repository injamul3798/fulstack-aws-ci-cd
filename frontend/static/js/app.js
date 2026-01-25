const API_URL = '/api/todos';

const todoInput = document.getElementById('todo-input');
const addBtn = document.getElementById('add-btn');
const todoList = document.getElementById('todo-list');
const itemsLeft = document.getElementById('items-left');
const clearCompleted = document.getElementById('clear-completed');
const filterBtns = document.querySelectorAll('.filter-btn');

let currentFilter = 'all';

async function fetchTodos() {
    try {
        const response = await fetch(API_URL);
        const todos = await response.json();
        renderTodos(todos);
    } catch (error) {
        console.error('Error fetching todos:', error);
    }
}

function renderTodos(todos) {
    let filteredTodos = todos;
    if (currentFilter === 'active') {
        filteredTodos = todos.filter(t => !t.completed);
    } else if (currentFilter === 'completed') {
        filteredTodos = todos.filter(t => t.completed);
    }

    todoList.innerHTML = '';
    filteredTodos.forEach(todo => {
        const li = document.createElement('li');
        li.className = `todo-item ${todo.completed ? 'completed' : ''}`;
        li.innerHTML = `
            <div class="checkbox-wrapper">
                <input type="checkbox" ${todo.completed ? 'checked' : ''} onchange="toggleTodo(${todo.id}, this.checked)">
            </div>
            <div class="todo-content">
                <span class="todo-title">${todo.title}</span>
            </div>
            <button class="delete-btn" onclick="deleteTodo(${todo.id})">×</button>
        `;
        todoList.appendChild(li);
    });

    const activeCount = todos.filter(t => !t.completed).length;
    itemsLeft.innerText = `${activeCount} item${activeCount !== 1 ? 's' : ''} left`;
}

async function addTodo() {
    const title = todoInput.value.trim();
    if (!title) return;

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, completed: false })
        });
        if (response.ok) {
            todoInput.value = '';
            fetchTodos();
        }
    } catch (error) {
        console.error('Error adding todo:', error);
    }
}

async function toggleTodo(id, completed) {
    try {
        await fetch(`${API_URL}/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ completed })
        });
        fetchTodos();
    } catch (error) {
        console.error('Error toggling todo:', error);
    }
}

async function deleteTodo(id) {
    try {
        await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
        fetchTodos();
    } catch (error) {
        console.error('Error deleting todo:', error);
    }
}

addBtn.addEventListener('click', addTodo);
todoInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') addTodo();
});

filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentFilter = btn.dataset.filter;
        fetchTodos();
    });
});

clearCompleted.addEventListener('click', async () => {
    // Note: A real implementation would have a bulk delete endpoint
    const response = await fetch(API_URL);
    const todos = await response.json();
    const completedTodos = todos.filter(t => t.completed);

    for (const todo of completedTodos) {
        await deleteTodo(todo.id);
    }
});

// Initial fetch
fetchTodos();

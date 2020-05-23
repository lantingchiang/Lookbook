// actions/todos.js

import axios from 'axios';
import { reset } from 'redux-form';
import history from '../history';
import { GET_TODOS, ADD_TODO, DELETE_TODO, EDIT_TODO } from './types';

// GET TODOS
export const getTodos = id => async dispatch => {
    const res = await axios.get('/api/todos/');
    dispatch({
        type: GET_TODOS,
        payload: res.data
    });
};

// ADD TODO
export const addTodo = formValues => async dispatch => {
    const res = await axios.post('/api/todos/', { ...formValues });
    dispatch({
        type: ADD_TODO,
        payload: res.data
    });
    dispatch(reset('todoForm'));
};

// DELETE TODO
export const deleteTodo = id => async dispatch => { // added
    await axios.delete(`/api/todos/${id}/`);
    dispatch({
        type: DELETE_TODO,
        payload: id
    });
    history.push('/');
};

// EDIT TODO
export const editTodo = (id, formValues) => async dispatch => {
    const res = await axios.patch(`/api/todos/${id}/`, formValues);
    dispatch({
        type: EDIT_TODO,
        payload: res.data
    });
    history.push('/');
};
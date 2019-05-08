import { get, post, put, deleteAjax } from './api.js';

export default {
    index: p => get('api/init-index/', p),
    blog: id => get(`api/blog/${id}/`, null),
    blogs: p => get('api/blog/', p),
    heart: p => post('api/blog/heart/', p),
    blogComment: p => get('api/comment/blog/', p),
    createComment: p => post(`api/comment/`, p),
    changeComment: (id, p) => put(`api/comment/${id}/`, p),
    deleteComment: id => deleteAjax(`api/comment/${id}/`, null),
    login: p => post('api/users/login/', p),
    register: p => post('api/users/register/', p),
    logout: () => post('api/users/logout/', null),
    tab: () => get('api/tab/', null),
    tabQuery: p => get('api/tab/query/', p),
    category: () => get('api/category/', null),
    categoryQuery: p => get('api/category/query/', p),
    aboutMe: () => get('api/about-me/', null),
}

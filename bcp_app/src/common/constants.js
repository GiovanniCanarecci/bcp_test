export const API_URL = process.env.REACT_APP_HTTP_PROXY || window.HTTP_PROXY || 'http://127.0.0.1:8000';

export const API = {
    employees: `${API_URL}/employees`,
    roles: `${API_URL}/roles`,
    customer_roles: `${API_URL}/customer_roles`,
    roles_synchronize: `${API_URL}/roles/synchronize`,
};

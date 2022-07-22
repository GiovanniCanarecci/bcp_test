import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom'; 
import { API } from '../../common/constants.js'; 
import './index.scss';

const RoleSynchronization = ({ setBackgroundState }) => {
    const navigate = useNavigate();
    const [customer_roles, setCustomerRoles] = useState([]);
    const [employees, setEmployees] = useState([]);
    const [formData, setFormData] = useState({ employee: '', new_customer_roles: [] });
    const { employee, new_customer_roles } = formData;

    useEffect(() => {
        setBackgroundState(0);

        fetch(API.employees, {
            method: 'GET',
            headers: {
                accept: 'application/json',
                'Content-Type': 'application/json',
            },
        }).then(res => res.json().then(c => {
            const [first_emp] = c;

            setEmployees(c);
            setFormData(oldFormData => ({ ...oldFormData, employee: first_emp.id }));
        }));

        fetch(API.customer_roles, {
            method: 'GET',
            headers: {
                accept: 'application/json',
                'Content-Type': 'application/json',
            },
        }).then(res => res.json().then(c => {
            setCustomerRoles(c);
        }));

    }, []);

    const onChangeRole = e => {
        let newRoles = [...new_customer_roles];
        const id = parseInt(e.target.value, 10);
    
        if(e.target.checked) {
            newRoles.push(id);
        } else {
            newRoles = newRoles.filter(v => v !== id);
        }
    
        setFormData(oldFormData => ({ ...oldFormData, new_customer_roles: newRoles }));
    };

    const handleSubmit = e => {
        e.preventDefault();

        fetch(API.roles_synchronize, {
            method: 'POST',
            headers: {
                accept: 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                employee_id: employee,
                new_customer_roles: new_customer_roles,
            }),
        }).then(res => res.json().then(data => navigate('/role', { state: { data, new_customer_roles } })));
    };

    const handleChange = e => {
        const { name, value } = e.target;

        setFormData({ ...formData, [name]: parseInt(10, value) });
    };

    return (
        <form id='roles-form' onSubmit={handleSubmit}>
            <h1>
                Select an employee and the new roles
            </h1>
            <label className='form-label'>
                <span>
                    Employee:
                </span>
                <select name='employee' value={employee} onChange={handleChange}>
                    {employees.map(({ id, name }) => (
                        <option key={id} value={id}>
                            {name}
                        </option>
                    ))}
                </select>
            </label>
            <span className='title-roles'>
                New roles:
            </span>
            {customer_roles.map(role => (
                <label key={role.id} className='role-checkbox'>
                    <input type='checkbox' name='role' value={role.id} onChange={onChangeRole} />
                    <span>
                        {role.name}
                    </span>
                </label>
            ))}
            <input type='submit' value='Update roles' />
        </form>
    );
};
// disabled={!new_customer_roles.length}

export default RoleSynchronization;

import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import './index.scss';

const keyNameMap = {
    deletedRoles: 'Deleted roles',
    addedRoles: 'Added roles',
    unchangedRoles: 'Unchanged roles',
    ignoredRoles: 'Ignored roles',
};

const RoleNew = ({ setBackgroundState }) => {
    // { "deletedRoles": [], "addedRoles": [], "unchangedRoles": ["BC_CLINICAL"], "ignoredRoles": ["BC_ADMIN","BC_WAREHOUSE"] }
    const { deletedRoles, addedRoles, unchangedRoles, ignoredRoles } = useLocation().state.data;

    const roles = { deletedRoles, addedRoles, unchangedRoles, ignoredRoles };

    useEffect(() => {
        setBackgroundState(1);
    }, []);
    return (
        <section id='new-role'>
            {Object.keys(roles).map(role => (
                <section key={role} className='role-box'>
                    <h2>{keyNameMap[role]}</h2>
                        {roles[role].length ? (
                            <ul>
                                {roles[role].map(roleStr => (
                                    <li key={roleStr}>
                                        {roleStr}
                                    </li>
                                ))}
                            </ul>
                        ) : <span className='no-results'>No results</span>}
                </section>
            ))}
        </section>
    );
};

export default RoleNew;
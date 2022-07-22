import { useState } from 'react';
import { BrowserRouter, Routes, Route, } from 'react-router-dom';
import MainNav from './common/components/main-nav/index.js';
import BrandBackground from './common/components/brand-background/index.js';
import RoleSynchronization from './views/role-synchronization/index.js';
import NewRoles from './views/role-new/index.js';

const Router = () => {
    const [backgroundState, setBackgroundState] = useState(0);

    return (
        <BrowserRouter>
            <MainNav />
            <BrandBackground state={backgroundState} />
            <Routes>
                <Route index element={<RoleSynchronization setBackgroundState={setBackgroundState} />} />
                <Route path='role' element={<NewRoles setBackgroundState={setBackgroundState} />} />
            </Routes>
        </BrowserRouter>
    );
};

export default Router;

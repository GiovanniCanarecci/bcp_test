import { Link } from 'react-router-dom';
import './index.scss';

const MainNav = () => (
    <header className='main-nav'>
        <Link to='/'>
            <h1>BCP test</h1>
        </Link>
    </header>
);

export default MainNav;

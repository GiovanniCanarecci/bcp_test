import clouds from '../../static/clouds.png';
import customIcon from '../../static/paper-plane.svg';
import './index.scss';

const BrandBackground = ({ state }) => (
    <div className={`brand-background state-${state}`} style={{ backgroundImage: `url(${clouds})` }}>
        <img src={customIcon} alt='' />
    </div>
);

export default BrandBackground;
import { StrictMode } from 'react';
import ReactDOM from 'react-dom/client';
import Router from './router.js';
// import reportWebVitals from './reportWebVitals';
import './common/styles/_variables.scss';
import './common/styles/_keyframes.scss';
import './index.scss';

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
    <StrictMode>
        <Router />
    </StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();

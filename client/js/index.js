import React from "react";
import ReactDOM from "react-dom";
import { Provider } from 'react-redux';

// rorutes
import Routes from './routes';

import '../css/bulma/bulma.sass';
import '../css/responsive.scss';

import ConfigureStore from './store/ConfigureStore';

const store = ConfigureStore();

ReactDOM.render(
  <Provider store={store}>
    <Routes />
  </Provider>
  , document.getElementById('app'));

import React from 'react';
import ReactDOM from 'react-dom';
import App from "./app/App";

import "rc-tooltip/assets/bootstrap.css";
import "./index.css";


ReactDOM.render(
  <App />,
  document.getElementById('root')
);

// eslint-disable-next-line no-undef
module.hot.accept();
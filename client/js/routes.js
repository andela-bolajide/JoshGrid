import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

// components
import HomeComponent from './components/HomePage/Home.component'

const Router = BrowserRouter;

class Routes extends React.Component {
  render() {
    return (
      <Router>
          <Switch>
            <Route exact path='/' component={ HomeComponent } />
          </Switch>
      </Router>
    )
  }
}

export default Routes;

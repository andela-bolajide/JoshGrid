import React from 'react';

// component
import Footer from '../../common/footer/Footer.component';
//import TextInput from 'grommet/components/TextInput';
import {Button, IconButton} from 'react-toolbox/lib/button';

// styles
import './home.scss';

class HomeComponent extends React.Component {
  constructor(props){
    super(props);
  }

  render() {
    return (
      <div className="home-container">
        <div className="home-body">
          <h1> JOSHGRID </h1>
          <div id="login-container">
            <input name="username" type="text" />
            <input name="password" type="password" />
          </div>
        </div>
        <Footer />
      </div>
    )
  }
}

export default HomeComponent;

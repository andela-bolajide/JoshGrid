import React from 'react';
import TypedText from '../../common/TypedText.jsx';

// component
import Footer from '../Footer/Footer.component';

// styles
import './Home.scss';

class HomeComponent extends React.Component {
  constructor(props){
    super(props);
  }

  render() {
    // const typed = new Typed('.element', {
    //   stringsElement: '#typed-strings'
    // });
    return (
      <div className="home-container">
        <div className="jg-brandname">
          <h1> JOSHGRID </h1> 
        </div>
        <div id="home-body">
          <div id="login-form">
            <input className="jg-input" name="username" type="text" placeholder="Username" />
            <input className="jg-input" name="password" type="password" placeholder="Password" />
            <div className="control">
              <button id="login-button" className="button is-primary">Login</button>
            </div>
            <span className="cta-signup">New to JOSHGRID? <a href="#">Sign Up</a></span>
          </div>
              <div className="jg-container">
                <TypedText
                  strings={[
                    'Some <i>strings</i> are slanted',
                    'Some <strong>strings</strong> are bold',
                    'HTML characters &times; &copy;'
                  ]}
                />
              <span id="typed"></span>
              </div>
        </div>
        <Footer />
      </div>
    )
  }
}

export default HomeComponent;

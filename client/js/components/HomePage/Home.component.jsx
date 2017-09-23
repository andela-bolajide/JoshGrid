import React from 'react';

// component
import Footer from '../Footer/Footer.component';

// styles
import './Home.scss';

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
          <section className="hero">
            <div className="hero-body">
              <div className="container">
                <h1 className="title">
                  Hero title
                </h1>
                <h2 className="subtitle">
                  Hero subtitle
                </h2>
              </div>
            </div>
          </section>
        </div>
        <Footer />
      </div>
    )
  }
}

export default HomeComponent;

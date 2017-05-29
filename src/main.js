const React = require('react');
const ReactDOM = require('react-dom');

class HelloWorld extends React.Component {
  render() {
    return (
      <div>
          <h1> Hello World </h1>
          <p> Bolaji Olajide 'Nuel </p>
      </div>
    )
  }
}

// Copy code here:
ReactDOM.render(<HelloWorld />, document.getElementById('root'));

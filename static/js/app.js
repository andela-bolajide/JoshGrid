webpackJsonp([0],{103:function(e,t,n){e.exports=n(104)},104:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{default:e}}var o=n(5),u=r(o),a=n(119),l=r(a),i=n(196),c=n(222),f=r(c);n(256),n(257);var s=n(258),d=r(s),p=(0,d.default)();l.default.render(u.default.createElement(i.Provider,{store:p},u.default.createElement(f.default,null)),document.getElementById("app"))},222:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{default:e}}function o(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function u(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function a(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}Object.defineProperty(t,"__esModule",{value:!0});var l=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}(),i=n(5),c=r(i),f=n(223),s=n(250),d=r(s),p=f.BrowserRouter,y=function(e){function t(){return o(this,t),u(this,(t.__proto__||Object.getPrototypeOf(t)).apply(this,arguments))}return a(t,e),l(t,[{key:"render",value:function(){return c.default.createElement(p,null,c.default.createElement(f.Switch,null,c.default.createElement(f.Route,{exact:!0,path:"/",component:d.default})))}}]),t}(c.default.Component);t.default=y},250:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{default:e}}function o(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function u(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function a(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}Object.defineProperty(t,"__esModule",{value:!0});var l=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}(),i=n(5),c=r(i),f=n(251),s=r(f),d=n(253),p=r(d);n(255);var y=function(e){function t(e){return o(this,t),u(this,(t.__proto__||Object.getPrototypeOf(t)).call(this,e))}return a(t,e),l(t,[{key:"render",value:function(){return c.default.createElement("div",{className:"home-container"},c.default.createElement("div",{className:"jg-brandname"},c.default.createElement("h1",null," JOSHGRID ")),c.default.createElement("div",{id:"home-body"},c.default.createElement("div",{id:"login-form"},c.default.createElement("input",{className:"jg-input",name:"username",type:"text",placeholder:"Username"}),c.default.createElement("input",{className:"jg-input",name:"password",type:"password",placeholder:"Password"}),c.default.createElement("div",{className:"control"},c.default.createElement("button",{id:"login-button",className:"button is-primary"},"Login")),c.default.createElement("span",{className:"cta-signup"},"New to JOSHGRID? ",c.default.createElement("a",{href:"#"},"Sign Up"))),c.default.createElement("div",{className:"jg-container"},c.default.createElement(s.default,{strings:["Some <i>strings</i> are slanted","Some <strong>strings</strong> are bold","HTML characters &times; &copy;"]}),c.default.createElement("span",{id:"typed"}))),c.default.createElement(p.default,null))}}]),t}(c.default.Component);t.default=y},251:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{default:e}}function o(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function u(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function a(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}Object.defineProperty(t,"__esModule",{value:!0});var l=function(){function e(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}return function(t,n,r){return n&&e(t.prototype,n),r&&e(t,r),t}}(),i=n(5),c=r(i),f=n(252),s=r(f),d=function(e){function t(){return o(this,t),u(this,(t.__proto__||Object.getPrototypeOf(t)).apply(this,arguments))}return a(t,e),l(t,[{key:"componentDidMount",value:function(){var e=this.props.strings,t={strings:e,typeSpeed:50,backSpeed:50};this.typed=new s.default(this.el,t),this.typed.loop=!0}},{key:"componentWillUnmount",value:function(){this.typed.destroy()}},{key:"render",value:function(){var e=this;return c.default.createElement("div",{className:"jg-typed-text"},c.default.createElement("div",{className:"title"},c.default.createElement("span",{style:{whiteSpace:"pre"},ref:function(t){e.el=t}})))}}]),t}(c.default.Component);t.default=d},253:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=n(5),o=function(e){return e&&e.__esModule?e:{default:e}}(r);n(254);var u=function(){return o.default.createElement("footer",{className:"site-footer"},o.default.createElement("span",{className:"footer-text"},"© Copyright 2017. JoshGrid Inc."))};t.default=u},254:function(e,t){},255:function(e,t){},256:function(e,t){},257:function(e,t){},258:function(e,t,n){"use strict";function r(e){return e&&e.__esModule?e:{default:e}}function o(e){return(0,u.createStore)(c.default,e,(0,u.applyMiddleware)(l.default))}Object.defineProperty(t,"__esModule",{value:!0}),t.default=o;var u=n(52),a=n(259),l=r(a),i=n(260),c=r(i)},260:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=n(52),o=n(261),u=function(e){return e&&e.__esModule?e:{default:e}}(o),a=(0,r.combineReducers)({JG:u.default});t.default=a},261:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};switch((arguments.length>1&&void 0!==arguments[1]?arguments[1]:{}).type){case"action1":return{value:"some text"};default:return e}};t.default=r}},[103]);
//# sourceMappingURL=app.js.map
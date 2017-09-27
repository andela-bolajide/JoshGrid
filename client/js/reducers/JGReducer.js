/**
 * Sample reducer definition.
 * @param {object} state the state you'd like to alter
 * @param {object} action the action to be processed
 * @returns {object} the state modified or not modified
 */
const JGReducer = (state = {}, action = {}) => {
  switch (action.type) {
    case 'action1':
      return {
        value: 'some text'
      };

    default:
      return state;
  }
};

export default JGReducer;

import { combineReducers } from 'redux';
import JG from './JGReducer';

// Combine all reducers
const RootReducer = combineReducers({
  JG
});

export default RootReducer;

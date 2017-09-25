export default function JGReducer (state={}, action={}) {
  switch(action.type) {
    case 'action1': 
      return {
        value: "some text"
      }
    default:
      return {
        value: "no value"
    }
  }
}
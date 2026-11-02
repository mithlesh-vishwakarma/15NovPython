import React, { Component } from 'react';

class UserGreetingClass extends Component {
  render() {
    const { username } = this.props;
    return (
      <div className="greeting-box class-greeting">
        <p>Class Component: <strong>Hello, {username}!</strong></p>
      </div>
    );
  }
}

export default UserGreetingClass;


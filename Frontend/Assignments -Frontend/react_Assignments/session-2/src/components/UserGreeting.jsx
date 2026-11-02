import React from 'react';

function UserGreeting({ username }) {
  return (
    <div className="greeting-box functional-greeting">
      <p>Functional Component: <strong>Hello, {username}!</strong></p>
    </div>
  );
}

export default UserGreeting;


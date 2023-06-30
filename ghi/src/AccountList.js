import React from "react";

function AccountList() {
  return (
    <table className="table table-dark table-striped">
      <h2>Map function for table</h2>
      <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Phone Number</th>
          <th>Address</th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>first name</td>
          <td>last naem</td>
          <td>phone #</td>
          <td>address</td>
        </tr>
      </tbody>
    </table>
  );
}

export default AccountList;

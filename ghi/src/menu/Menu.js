import React from "react";

export default function Menu({ menuItems }) {
  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
          <h1>Menu</h1>
        </div>
      </div>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Category</th>
            <th>Name</th>
            <th>Picture</th>
            <th>Description</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          {menuItems?.map((menuItem) => {
            return (
              <tr key={menuItem.id}>
                <td>{menuItem.category}</td>
                <td>{menuItem.name}</td>
                <td>{menuItem.picture_url}</td>
                <td>{menuItem.description}</td>
                <td>{menuItem.price}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

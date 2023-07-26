import { useState, useEffect } from "react";

function MenuItemsTable() {
  const [menuItems, setMenuItems] = useState([]);

  useEffect(() => {
    async function getMenuItems() {
      const url = `${process.env.REACT_APP_API_HOST}/menu_items/`;
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setMenuItems(data.menuItems);
      } else {
        console.error(response);
      }
    }
    getMenuItems();
  }, []);

  return (
    <div>
      <h1>Menu Items</h1>
      <table className="table table-striped table-hover">
        <thead>
          <tr>
            <th>ID</th>
            <th>Category</th>
            <th>Name</th>
            <th>Picture URL</th>
            <th>Description</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          {menuItems.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.category}</td>
              <td>{item.name}</td>
              <td>{item.picture_url}</td>
              <td>{item.description}</td>
              <td>{item.price}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default MenuItemsTable;

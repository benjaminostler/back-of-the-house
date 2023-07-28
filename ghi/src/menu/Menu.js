import { Link } from "react-router-dom";

const baseURL = `${process.env.REACT_APP_API_HOST}/menu_items`;
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
            <th>Quantity</th>
          </tr>
        </thead>
        <tbody>
          {menuItems.map((item) => (
            <tr key={item.id}>
              <td>{item.category}</td>
              <td>
                <Link to={baseURL + item.id}>{item.name}</Link>
              </td>
              <td>
                <img
                  className="img-thumbnail"
                  alt="Menu item "
                  width="100px"
                  height="100px"
                  src={item.picture_url}
                />
              </td>
              <td>{item.description}</td>
              <td>{item.price}</td>
              <td> 0 waiting for incrementer </td>
              <td>
                <button className="btn  btn-danger  mx-3">Add to Cart</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

// Need a function that adds an item to a cart, or starts an order

// handle function?

// <button
//   onClick={() => {
//
//    add to cart function?
//     /not  sure what to do here except add it to our cart, or maybe start an order
//   }}

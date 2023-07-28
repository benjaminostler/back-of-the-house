import { Link } from "react-router-dom";
import {
  addToCart,
  incrementQuantity,
  decrementQuantity,
  enterQuantity,
} from "../features/cart/CartSlice";
import { useDispatch } from "react-redux";

const baseURL = `${process.env.REACT_APP_API_HOST}/menu_items/`;
export default function Menu({ menuItems }) {
  const dispatch = useDispatch();

  const handleIncrementQuantity = (id) => {
    dispatch(incrementQuantity(id));
  };

  const handleDecrementQuantity = (id) => {
    dispatch(decrementQuantity(id));
  };

  const handleEnterQuantity = (id, quantity) => {
    dispatch(enterQuantity({ id, quantity }));
  };

  const handleAddToCart = (item) => {
    dispatch(addToCart(item));
  };
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
                  alt={item.description}
                  width="100px"
                  height="100px"
                  src={item.picture_url}
                />
              </td>
              <td>{item.description}</td>
              <td>{item.price}</td>

              <td>
                <button onClick={() => handleIncrementQuantity(item.id)}>
                  +
                </button>
                {/* possibly delete these if you cant get it to work */}

                <input
                  onClick={() => handleEnterQuantity(item.id)}
                  type="number"
                  min="1"
                  defaultValue={1}
                  onChange={(e) =>
                    handleEnterQuantity(item.id, parseInt(e.target.value))
                  }
                />

                <button onClick={() => handleDecrementQuantity(item.id)}>
                  -
                </button>
              </td>
              <td>
                <button
                  className="btn  btn-danger  mx-3"
                  onClick={() => handleAddToCart(item)}
                >
                  Add to Cart
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

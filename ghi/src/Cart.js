import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import {
  addToCart,
  incrementQuantity,
  decrementQuantity,
  enterQuantity,
  removeItem,
} from "./features/cart/CartSlice";

const Cart = () => {
  const dispatch = useDispatch();
  const cart = useSelector((state) => state.cart.cart);
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetchItems();
  }, []);

  async function fetchItems() {
    const response = await fetch("http://localhost:8000/menu_items");
    const items = await response.json();

    if (items.message) {
      setItems([]);
    } else {
      setItems(items);
    }
  }
  const calculateSubTotal = () => {
    const totalPrice = cart.reduce(
      (total, item) => total + item.price * item.quantity,
      0
    );
    return totalPrice.toFixed(2);
  };
  const calculateTotalPrice = () => {
    const totalPrice = cart.reduce(
      (total, item) => total + item.price * item.quantity * 1.0975,
      0
    );
    return totalPrice.toFixed(2);
  };

  const handleAddToCart = (item) => {
    dispatch(addToCart(item));
  };

  const handleIncrementQuantity = (id) => {
    dispatch(incrementQuantity(id));
  };

  const handleDecrementQuantity = (id) => {
    dispatch(decrementQuantity(id));
  };

  const handleEnterQuantity = (id, quantity) => {
    dispatch(enterQuantity({ id, quantity }));
  };

  const handleRemoveItem = (id) => {
    dispatch(removeItem(id));
  };

  return (
    <div>
      <h1>Shopping Cart</h1>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Qty</th>
            <th>Price</th>
            <th>Add/Subtract</th>
          </tr>
        </thead>
        <tbody>
          {cart.map((item) => (
            <tr key={item.id}>
              <td>{item.name}</td>
              <td>{item.quantity}</td>
              <td>${item.price}</td>
              <td>
                <button onClick={() => handleIncrementQuantity(item.id)}>
                  +
                </button>
                <button onClick={() => handleDecrementQuantity(item.id)}>
                  -
                </button>
                <input
                  type="number"
                  min="1"
                  defaultValue={1}
                  onChange={(e) =>
                    handleEnterQuantity(item.id, parseInt(e.target.value))
                  }
                />
              </td>
              <td>
                <button onClick={() => handleRemoveItem(item.id)}>
                  Remove
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <h4>Sub-total:${calculateSubTotal()}</h4>
      <h3 className="strong">Total: ${calculateTotalPrice()}</h3>
      <div>
        <h2>Menu Items</h2>
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Picture</th>
              <th>Add to Cart</th>
            </tr>
          </thead>
          <tbody>
            {items.map((item) => (
              <tr key={item.id}>
                <td>{item.name}</td>
                <td>
                  <img src={item.image_url} alt={item.description} />
                </td>
                <td>
                  <button onClick={() => handleAddToCart(item)}>
                    Add to Cart
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Cart;

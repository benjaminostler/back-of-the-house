import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { useEffect, useState } from "react";
import {
  incrementQuantity,
  decrementQuantity,
  enterQuantity,
  removeItem,
} from "./features/cart/CartSlice";
import cartanim from "./assets/lottie_files/shopping_cart.json";
import Lottie from "lottie-react";

const Cart = () => {
  const dispatch = useDispatch();
  const cart = useSelector((state) => state.cart.cart);
  const [items, setItems] = useState([]);
  console.log(items);
  useEffect(() => {
    fetchItems();
  }, []);

  async function fetchItems() {
    const response = await fetch("http://localhost:8000/menu_items/");
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
    <div className="container">
      <div className="row">
        <div className="col-4" style={{ "background-color": "black" }}>
          <Lottie animationData={cartanim} />
        </div>
        <div className="col-8">
          <h1>Cart</h1>
          <div className="shadow p-4 mt-4">
            <table className="table table-striped">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Qty</th>
                  <th>Price</th>
                  <th>+1/-1 Enter Qty</th>
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
          </div>
        </div>
      </div>
    </div>
  );
};

export default Cart;

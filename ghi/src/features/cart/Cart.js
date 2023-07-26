import React from "react";
import { useSelector } from "react-redux";
import CartItem from "./CartItem";

function Cart() {
  // assumes the cart reducer is named 'cart'
  const cart = useSelector((state) => state.cart);

  return (
    <div className="cart">
      <h1>Your Cart</h1>
      {cart.map((item) => (
        <CartItem key={item.id} item={item} />
      ))}
    </div>
  );
}

export default Cart;

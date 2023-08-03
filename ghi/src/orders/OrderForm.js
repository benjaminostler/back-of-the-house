import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import takingnotes from "../assets/lottie_files/taking_notes.json";
import Lottie from "lottie-react";

export default function OrderForm() {
  const [accountId, setAccountId] = useState("");
  const [subtotal, setSubtotal] = useState("");
  const [total, setTotal] = useState("");
  const navigate = useNavigate();
  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = {
      account_id: accountId,
      subtotal,
      total,
    };
    const orderUrl = `${process.env.REACT_APP_API_HOST}/order`;
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch(orderUrl, fetchConfig);
    if (response.ok) {
      const newOrder = await response.json();
      console.log("new order Item", newOrder);

      setSubtotal("");
      setTotal("");
      navigate("/");
    }
  };

  const handleAccountIdChange = (event) => {
    setAccountId(event.target.value);
  };

  const handleSubtotalChange = (event) => {
    setSubtotal(event.target.value);
  };
  const handleTotalChange = (event) => {
    setTotal(event.target.value);
  };

  return (
    <div className="container">
      <div className="row">
        <div className="col-5">
          <Lottie animationData={takingnotes} />
        </div>
        <div className="col-7">
          <div className="shadow p-4 mt-4">
            <h1>Create an Order</h1>
            <form onSubmit={handleSubmit} id="create-order-form">
              <div className="form-floating mb-3">
                <input
                  onChange={handleAccountIdChange}
                  placeholder="Account ID"
                  required
                  value={accountId}
                  type="text"
                  name="account_id"
                  id="account_id"
                  className="form-control"
                />
                <label htmlFor="account_id">Account ID</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  onChange={handleSubtotalChange}
                  placeholder="Subtotal"
                  required
                  value={subtotal}
                  type="text"
                  name="subtotal"
                  id="subtotal"
                  className="form-control"
                />
                <label htmlFor="subtotal">Subtotal</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  onChange={handleTotalChange}
                  placeholder="Order Total"
                  required
                  value={total}
                  type="text"
                  name="total"
                  id="total"
                  className="form-control"
                />
                <label htmlFor="total">Total</label>
              </div>
              <button type="submit" className="btn btn-outline-primary">
                Submit Order
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

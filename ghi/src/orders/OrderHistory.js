import React from "react";
import { useEffect, useState } from "react";
import history from "../assets/lottie_files/order_history.json";
import Lottie from "lottie-react";

export default function OrderHistory() {
  const [orders, setOrders] = useState([]);

  async function getOrders() {
    const url = `${process.env.REACT_APP_API_HOST}/order`;
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setOrders(data);
    } else {
      console.error(response);
    }
  }

  useEffect(() => {
    getOrders();
  }, []);

  return (
    <div className="container">
      <div className="row">
        <div className="col-8 shadow p-4 mt-4">
          <h1>Order History</h1>
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Order Id</th>
                <th>Subtotal</th>
                <th>Total</th>
              </tr>
            </thead>
            <tbody>
              {orders.map((ord) => (
                <tr key={ord.id}>
                  <td>{ord.id}</td>
                  <td>${ord.subtotal}</td>
                  <td>${ord.total}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div className="col-4">
          <Lottie animationData={history} />
        </div>
      </div>
    </div>
  );
}

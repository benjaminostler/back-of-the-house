function OrderItem({ id, subtotal, total }) {
  return (
    <div className="orderItem">
      <div className="orderItem__info">
        <p className="orderItem__subtotal">
          <strong>{id}</strong>
        </p>
        <p className="orderItem__subtotal">
          <small>$</small>
          <strong>{subtotal}</strong>
        </p>
        <p className="orderItem__total">
          <small>$</small>
          <strong>{total}</strong>
        </p>
      </div>
    </div>
  );
}

export default OrderItem;

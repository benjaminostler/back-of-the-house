import { configureStore } from "@reduxjs/toolkit";
import { cartReducer } from "../features/cart/CartSlice";
import { orderReducer } from "../features/Order/OrderSlice"

export const store = configureStore({
  reducer: {
    cart: cartReducer,
    order: orderReducer,
  },
});

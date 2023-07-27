import { configureStore } from "@reduxjs/toolkit";
import { cartReducer } from "../features/cart/CartSlice";
0;

export const store = configureStore({
  reducer: {
    cart: cartReducer,
  },
});

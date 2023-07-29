// src/redux/orderSlice.js
import { createSlice } from "@reduxjs/toolkit";

const orderSlice = createSlice({
  name: "order",
  initialState: {
    order: [],
  },
  reducers: {
    addToOrder: (state, action) => {
      state.order.push({ ...action.payload });
    }
  },
});

export const orderReducer = orderSlice.reducer;
export const {
  addToOrder,
} = orderSlice.actions;
export default orderSlice.reducer;

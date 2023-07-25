import { createSlice } from "@reduxjs/toolkit";

const cartSlice = createSlice({
  name: "cart",
  initialState: [],
  reducers: {
    addToCart: (state, action) => {
      // Check if item is already in the cart
      const itemIndex = state.findIndex(
        (item) => item.id === action.payload.id
      );

      // If item is new, add it to the cart
      if (itemIndex === -1) {
        state.push(action.payload);
      }
      // If item already exists in cart, increment the quantity
      else {
        state[itemIndex].quantity += action.payload.quantity;
      }
    },
    removeFromCart: (state, action) => {
      // Return all items except the one we want to remove
      return state.filter((item) => item.id !== action.payload.id);
    },
    updateQuantity: (state, action) => {
      // Find index of item in cart
      const itemIndex = state.findIndex(
        (item) => item.id === action.payload.id
      );

      // If the item is found in the cart, update the quantity
      if (itemIndex !== -1) {
        state[itemIndex].quantity = action.payload.quantity;
      }
    },
    clearCart: () => {
      // Return a new empty array to clear the cart
      return [];
    },
    // more actions like increase/decrease quantity, clear cart, etc
  },
});

export const { addToCart, removeFromCart, updateQuantity, clearCart } =
  cartSlice.actions;

export default cartSlice.reducer;

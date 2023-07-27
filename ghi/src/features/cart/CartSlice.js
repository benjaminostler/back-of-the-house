// src/redux/cartSlice.js
import { createSlice } from "@reduxjs/toolkit";

const cartSlice = createSlice({
  name: "cart",
  initialState: {
    cart: [],
  },
  reducers: {
    addToCart: (state, action) => {
      const itemInCart = state.cart.find(
        (item) => item.id === action.payload.id
      );
      if (itemInCart) {
        itemInCart.quantity++;
      } else {
        state.cart.push({ ...action.payload, quantity: 1 });
      }
    },
    incrementQuantity: (state, action) => {
      const item = state.cart.find((item) => item.id === action.payload);
      item.quantity++;
    },
    decrementQuantity: (state, action) => {
      const item = state.cart.find((item) => item.id === action.payload);
      if (item.quantity === 1) {
        item.quantity = 1;
      } else {
        item.quantity--;
      }
    },
    removeItem: (state, action) => {
      const removeItem = state.cart.filter(
        (item) => item.id !== action.payload
      );
      state.cart = removeItem;
    },
  },
});

export const cartReducer = cartSlice.reducer;
export const { addToCart, incrementQuantity, decrementQuantity, removeItem } =
  cartSlice.actions;

// import { createSlice } from "@reduxjs/toolkit";

// const cartSlice = createSlice({
//   name: "cart",
//   initialState: [],
//   reducers: {
//     addToCart: (state, action) => {
//       // Check if item is already in the cart
//       const itemIndex = state.findIndex(
//         (item) => item.id === action.payload.id
//       );

//       // If item is new, add it to the cart
//       if (itemIndex === -1) {
//         state.push(action.payload);
//       }
//       // If item already exists in cart, increment the quantity
//       else {
//         state[itemIndex].quantity += action.payload.quantity;
//       }
//     },
//     removeFromCart: (state, action) => {
//       // Return all items except the one we want to remove
//       return state.filter((item) => item.id !== action.payload.id);
//     },
//     updateQuantity: (state, action) => {
//       // Find index of item in cart
//       const itemIndex = state.findIndex(
//         (item) => item.id === action.payload.id
//       );

//       // If the item is found in the cart, update the quantity
//       if (itemIndex !== -1) {
//         state[itemIndex].quantity = action.payload.quantity;
//       }
//     },
//     clearCart: () => {
//       // Return a new empty array to clear the cart
//       return [];
//     },
//     // more actions like increase/decrease quantity, clear cart, etc
//   },
// });

// export const { addToCart, removeFromCart, updateQuantity, clearCart } =
//   cartSlice.actions;

export default cartSlice.reducer;

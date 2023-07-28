import { createSlice } from "@reduxjs/toolkit";

const MenuSlice = createSlice({
  name: "menu",
  initialState: {
    menu: [],
  },
  reducers: {
    incrementMenuItemQuantity: (state, action) => {
      const item = state.cart.find((item) => item.id === action.payload);
      item.quantity++;
    },
    decrementMenuItemQuantity: (state, action) => {
      const item = state.cart.find((item) => item.id === action.payload);
      if (item.quantity === 1) {
        item.quantity = 1;
      } else {
        item.quantity--;
      }
    },
    enterMenuItemQuantity: (state, action) => {
      const item = state.cart.find((item) => item.id === action.payload.id);
      item.quantity = action.payload.quantity;
    },
  },
});

export const MenuReducer = MenuSlice.reducer;
export const {
  incrementMenuItemQuantity,
  decrementMenuItemQuantity,
  enterMenuItemQuantity,
} = MenuSlice.actions;
export default MenuSlice.reducer;

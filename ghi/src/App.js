import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import { useState, useEffect } from "react";
import { AccountContext } from "./AccountContext";

import MainPage from "./MainPage.js";
import Nav from "./Nav.js";

import SignupForm from "./accounts/SignupForm.js";
import LoginForm from "./accounts/LoginForm.js";
import UpdateAccount from "./accounts/UpdateAccount";
import AccountDetails from "./accounts/AccountDetail.js";

import ReservationForm from "./reservations/ReservationForm.js";
import ReservationList from "./reservations/ReservationList.js";
import ReservationDetail from "./reservations/ReservationDetail.js";
import EditReservationForm from "./reservations/ReservationEditForm.js";

import Cart from "./Cart.js";

import MenuItemForm from "./menu/MenuItemForm.js";
import Menu from "./menu/Menu.js";
import MenuItemDetail from "./menu/MenuItemDetail.js";

import OrderHistory from "./orders/OrderHistory";


function App() {
  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, "");
  const [accountData, setAccountData] = useState(null);
  const [menuItems, setMenuItems] = useState([]);

  async function getMenuItems() {
    const url = `${process.env.REACT_APP_API_HOST}/menu_items/`;
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setMenuItems(data);
    } else {
      console.error(response);
    }
  }

  useEffect(() => {
    getMenuItems();
  }, []);

  return (
    <AccountContext.Provider value={{ accountData, setAccountData }}>
      <BrowserRouter basename={basename}>
        <AuthProvider baseUrl={process.env.REACT_APP_API_HOST}>

          <Nav accountData={accountData} />

        <div className="container">

            <Routes>
              <Route path="/" element={<MainPage />} />
              <Route path="/signup" element={<SignupForm />} />
              <Route path="/loginform" element={<LoginForm />} />
              <Route path="/myaccount" element={<AccountDetails accountData={accountData} />} />
              <Route path="/editmyaccount" element={<UpdateAccount accountData={accountData} />} />

              <Route path="/cart" element={<Cart />} />

              <Route path="/orders" element={<OrderHistory/>} />
              <Route path="/reservations/:id" element = {<EditReservationForm />} />
              <Route path="/reservations/new" element={<ReservationForm />} />
              <Route path="/reservations" element={<ReservationList />} />
              <Route path="/reservations/:id" element={<ReservationDetail />} />

              <Route path="/menu_items">
                <Route index element={<Menu menuItems={menuItems} />} />
                <Route path=":id" element={<MenuItemDetail />} />
                <Route path="new" element={<MenuItemForm />} />
              </Route>

            </Routes>
          </div>
        </AuthProvider>
      </BrowserRouter>
    </AccountContext.Provider>
  );
}

export default App;

import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainPage from "./MainPage.js";
import Nav from "./Nav.js";
import SignupForm from "./accounts/SignupForm.js";
import LoginForm from "./accounts/LoginForm.js";
import ReservationForm from "./reservations/ReservationForm.js";
import ReservationList from "./reservations/ReservationList.js";
import ReservationDetail from "./reservations/ReservationDetail.js";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";
import MenuItemForm from "./menu/MenuItemForm.js";
import Menu from "./menu/Menu.js";
import MenuItemDetail from "./menu/MenuItemDetail.js";
import { useState, useEffect } from "react";

function App() {
  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, "");

  const [menuItems, setMenuItems] = useState([]);
  // const[selectedmenuItem, setselectedMenuItem]=useState("");

  async function getMenuItems() {
    const url = `http://localhost:8000/menu_items/`;
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      // console.log("menus", data);
      // console.log("data object", data[0]);
      // console.log("!!!!", data[0].picture_url);
      setMenuItems(data);
    } else {
      console.error(response);
    }
  }

  useEffect(() => {
    getMenuItems();
  }, []);

  return (
    <BrowserRouter basename={basename}>
      <AuthProvider baseUrl={process.env.REACT_APP_API_HOST}>
        <Nav />
        <div className="container">
          <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="/reservations/new" element={<ReservationForm />} />
            <Route path="/reservations" element={<ReservationList />} />
            <Route path="/reservations/:id" element={<ReservationDetail />} />
            <Route path="/accounts/new" element={<SignupForm />} />
            <Route path="/loginform" element={<LoginForm />} />

            <Route path="/menu">
              <Route index element={<Menu menuItems={menuItems} />} />

              <Route path=":id" element={<MenuItemDetail />} />
              <Route path="new" element={<MenuItemForm />} />
            </Route>
          </Routes>
        </div>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
